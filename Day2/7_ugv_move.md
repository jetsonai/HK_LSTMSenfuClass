# UGV 브링업

---------------------------------------------------------------

### 컨테이너 Attach 전이라면 

도커 Attach 전에 필수

xhost +

echo $DISPLAY

### 컨테이너 시작 전이라면 RHS

### 컨테이너 Attach 전이라면 RHA

----------------------------------------------------------------

# 1. UGV BringUp

export DISPLAY=:1

## 브링업

ros2 launch ugv_bringup bringup_lidar.launch.py use_rviz:=true

![image](https://github.com/user-attachments/assets/78e2c6c7-4776-4c73-9bdc-7cb3c968aed4)


## 드라이브 테스트 준비

다른 터미널 켜고 RHA


![image](https://github.com/user-attachments/assets/b43775ab-6996-44d1-ae6d-15e4b57e3d9b)


## 드라이브 테스트

ros2 run ugv_tools keyboard_ctrl

![image](https://github.com/user-attachments/assets/4ad83d26-1a7f-4b0b-a0d4-24980e18f415)

로봇이 테이블에서 떨어지지 않게 조심해서 한번씩 천천히 눌러주세요

## 라이다 보기

![image](https://github.com/user-attachments/assets/e4e039d3-0cef-49cd-957c-51bf7775a0df)

![image](https://github.com/user-attachments/assets/279359da-2253-4bfc-a275-202f4d776161)





