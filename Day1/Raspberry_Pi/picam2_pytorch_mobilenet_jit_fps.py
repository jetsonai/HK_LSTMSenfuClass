import time

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
    
    started = time.time()
    last_logged = time.time()
    frame_count = 0
    
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
    
            # 모델 성능 기록
            frame_count += 1
            now = time.time()
            if now - last_logged > 1:
                print(f"{frame_count / (now-last_logged)} fps")
                last_logged = now
                frame_count = 0


if __name__ == "__main__" :
    main()