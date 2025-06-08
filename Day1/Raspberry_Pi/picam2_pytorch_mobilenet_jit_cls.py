import time

import json

import torch
import numpy as np
from torchvision import models, transforms

import cv2
from picamera2 import Picamera2


def main() :
    # 안정성을 위해 Thread 사용 개수 제한
    torch.set_num_threads(2)
    torch.backends.quantized.engine = 'qnnpack'
    
    # Initialize the Picamera2
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (1280, 720)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.align()
    picam2.configure("preview")
    picam2.start()
    
    # 전처리 인스턴스 생성
    preprocess = transforms.Compose([transforms.ToTensor(),
                                     transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                                                          std=[0.229, 0.224, 0.225]),])
    
    net = models.quantization.mobilenet_v2(pretrained=True, quantize=True)
    # ~20fps에서 ~30fps로 향상시키는 JIT 모델
    net = torch.jit.script(net)
    net.eval()

    with open("imagenet_class_index.json") as file :
        class_idx = json.load(file)
    idx2label = [class_idx[str(k)][1] for k in range(len(class_idx))]
    
    with torch.no_grad():
        while True:
            # Capture frame-by-frame
            frame = picam2.capture_array()
            
            # Resize to 224x224
            img = cv2.resize(frame.copy(), (224,224))
    
            # OpenCV 출력을 BGR에서 RGB로 변환
            img = img[:, :, [2, 1, 0]]
    
            # 전처리(preprocessing)
            input_tensor = preprocess(img)
    
            # 모델에 의해 예상되는 미니 배치(mini-batch) 생성
            input_batch = input_tensor.unsqueeze(0)
    
            # 모델 실행
            output = net(input_batch)
            
            # 분류 결과 정렬
            top = list(enumerate(output[0].softmax(dim=0)))
            top.sort(key=lambda x: x[1], reverse=True)
                        
            # 이미지에 결과 출력
            h, w = frame.shape[:2]
            top_1_idx, top_1_val = top[0]
            frame = cv2.putText(img=frame, 
                                text=f"{top_1_val.item()*100:.2f}% {idx2label[top_1_idx]}", 
                                org=(w//16, int(h/1.5)), 
                                fontFace=cv2.FONT_HERSHEY_PLAIN, 
                                fontScale=5, 
                                color=(255,255,255), 
                                thickness=5, 
                                lineType=cv2.LINE_AA)
            
            # Display the resulting frame
            cv2.imshow("Camera", frame)
            
            # 분류 결과 출력
            for idx, val in top[:10]:
                print(f"{val.item()*100:.2f}% {idx2label[idx]}")
            print()
            
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) == ord("q"):
                break

# Release resources and close windows
cv2.destroyAllWindows()


if __name__ == "__main__" :
    main()