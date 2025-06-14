# RVIZ UGV Model

## show rviz

5번에서 계속 이어서

cd /home/ws/ugv_ws

ros2 launch ugv_description display.launch.py use_rviz:=true

![image](https://github.com/user-attachments/assets/7cebaf4d-bdd4-49df-b90f-7e7ef38e88a7)

RVIZ 화면이 뜹니다.

![image](https://github.com/user-attachments/assets/5fa68e48-8b13-4b75-a37c-84ffac8c34a5)

## 기능 시작

터미널을 하나 더 띄우고

RHE

ros2 run ugv_bringup ugv_driver

![image](https://github.com/user-attachments/assets/d2791717-1b6e-4076-a47c-45d81a8ba7dd)

## 기능 테스트

joint state publisher 를 제어해봅니다.

pt_base_link_to_pt_link1: 카메라 팬틸트의 좌우 방향을 제어합니다.
pt_link1_to_pt_link2: 카메라 팬틸트의 위아래 방향을 제어합니다.
Center: 카메라 팬틸트의 방향을 중앙에 맞춥니다.

![image](https://github.com/user-attachments/assets/4d6e7dd0-0018-4218-87d3-4151526e6c50)

## 라이트 테스트

터미널을 하나 더 켜고 RHE

### 라이트 켜기

ros2 topic pub /ugv/led_ctrl std_msgs/msg/Float32MultiArray "{data: [255, 255]}" -1

### 라이트 끄기

ros2 topic pub /ugv/led_ctrl std_msgs/msg/Float32MultiArray "{data: [0, 0]}" -1

![image](https://github.com/user-attachments/assets/36e41b6f-0e0f-4ed2-afe6-5f21dfb920e3)













