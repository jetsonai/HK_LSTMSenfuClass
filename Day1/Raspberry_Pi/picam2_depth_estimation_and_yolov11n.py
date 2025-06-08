import cv2
from picamera2 import Picamera2

import numpy as np

import torch

from ultralytics import YOLO


def main() :
    # Initialize the Picamera2
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (720, 360)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.align()
    picam2.configure("preview")
    picam2.start()

    # Load the MiDaS model
    model_type = "MiDaS_small"
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    midas.eval()

    # Load YOLOV11n Model
    yolov11n = YOLO("ckpt/yolo11n.pt")

    # Preprocessing Module
    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
    preprocess = midas_transforms.small_transform

    with torch.no_grad():
        while True:
            # Capture frame-by-frame
            frame = picam2.capture_array()
            
            # Resize to 224x224
            img = cv2.resize(frame.copy(), (640,360))
    
            # 전처리(preprocessing)
            input_tensor = preprocess(img)
    
            # 모델에 의해 예상되는 미니 배치(mini-batch) 생성
            input_batch = input_tensor
    
            # 모델 실행
            output = midas(input_batch)
            print(1/output)
            
            # Apply Min-Max Norm
            output = (output - output.min()) / (output.max() - output.min())

            # PyTorch Tensor -> Numpy Array
            output = output.permute(1,2,0).repeat(1,1,3).cpu().numpy()

            # [0,1] -> [0,255]
            output = (output*255).astype(np.uint8)

            # YOLOv11n
            results = yolov11n(frame, imgsz=640)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()
            h, w = annotated_frame.shape[:2]
            output_ = cv2.resize(output.copy(), (w,h))

            for result in results :
                xywh = result.boxes.xywhn # center-x, center-y, width, height
                if xywh.shape[0] != 0 :
                    center_x, center_y, width, height = xywh[0]
                    pt1, pt2 = [center_x-width/2, center_y-height/2], [center_x+width/2, center_y+height/2]
                    pt1[0], pt1[1] = int(pt1[0]*w), int(pt1[1]*h)
                    pt2[0], pt2[1] = int(pt2[0]*w), int(pt2[1]*h)
                    output_ = cv2.rectangle(output_, pt1, pt2, (0, 255, 0), 2)

            # Interpolation
            output = cv2.resize(output, (360, 360))
            annotated_frame = cv2.resize(annotated_frame, (360, 360))
            output_ = cv2.resize(output_, (360, 360))
            final_frame = np.hstack((output, annotated_frame, output_))

            # Display the resulting frame
            cv2.imshow("Camera", final_frame)
    
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) == ord("q"):
                break

# Release resources and close windows
cv2.destroyAllWindows()


if __name__ == "__main__" :
    main()