import torch
from torch import nn
from torchvision import transforms
from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights

import cv2


def main(num_classes, img_size, img_path) :
    # Model 인스턴스 생성
    model_frozen = mobilenet_v3_small(weights=MobileNet_V3_Small_Weights.DEFAULT)
    model_frozen.classifier[-1] = nn.Linear(1024, num_classes) # Customize Classifier
    model_unfrozen = mobilenet_v3_small(weights=MobileNet_V3_Small_Weights.DEFAULT)
    model_unfrozen.classifier[-1] = nn.Linear(1024, num_classes) # Customize Classifier

    # 모델 가중치 불러오기
    model_frozen.load_state_dict(torch.load("ckpt/frozen_best.pth", map_location=torch.device('cpu')), strict=True) # GPU -> CPU
    model_unfrozen.load_state_dict(torch.load("ckpt/unfrozen_best.pth", map_location=torch.device('cpu')), strict=True) # GPU -> CPU

    # 전처리 인스턴스 생성
    preprocess = transforms.Compose([transforms.ToTensor(),
                                     transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                                                          std=[0.229, 0.224, 0.225]),])
    
    model_frozen.eval()
    model_unfrozen.eval()
    
    with torch.no_grad():
        # Load Image
        img = cv2.imread(img_path)
        
        # Resize to 224x224
        img = cv2.resize(img, (224,224))

        # OpenCV 출력을 BGR에서 RGB로 변환
        img = img[:, :, [2, 1, 0]]

        # 전처리(preprocessing)
        input_tensor = preprocess(img)

        # 모델에 의해 예상되는 미니 배치(mini-batch) 생성
        input_batch = input_tensor.unsqueeze(0)

        # 모델 실행
        output_frozen = model_frozen(input_batch)
        output_unfrozen = model_unfrozen(input_batch)
        
        # Probability 계산
        prob_frozen = output_frozen.softmax(dim=-1)
        prob_unfrozen = output_unfrozen.softmax(dim=-1)
        prob_frozen_cat, prob_frozen_dog = prob_frozen[0][0]*100, prob_frozen[0][1]*100
        prob_unfrozen_cat, prob_unfrozen_dog = prob_unfrozen[0][0]*100, prob_unfrozen[0][1]*100
        
        # 결과 비교
        print(f"CNN Backbone Frozen : {prob_frozen_cat:.4f}% Cat | {prob_frozen_dog:.4f}% Dog")
        print(f"CNN Backbone Unfrozen : {prob_unfrozen_cat:.4f}% Cat | {prob_unfrozen_dog:.4f}% Dog")


if __name__ == "__main__" :
    num_classes = 2
    img_size = 224
    img_path_list = ["img/dog_1.jpg", "img/dog_2.jpg", "img/cat_1.jpg", "img/cat_2.jpg"]
    
    for img_path in img_path_list :
        print(f"[{img_path}]")
        main(num_classes, img_size, img_path)
        print()