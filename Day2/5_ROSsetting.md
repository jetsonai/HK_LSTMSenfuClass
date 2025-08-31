# ROS 환경 시작하기

![image](https://github.com/user-attachments/assets/2fb09f56-4191-472b-a85c-dce99cb7448a)

## 컨테이너 만들기

sudo docker run --privileged --name UGV_RPI_ROS -e DISPLAY=unix$DISPLAY -e='QT_X11_NO_MITSHM=1' -e IS_PERSISTENT=TRUE -e ANONYMIZED_TELEMETRY=TRUE --ipc=host -it -d --net=host -v /dev/snd:/dev/snd --volume='/docker_job:/docker_job' --volume='/tmp/.X11-unix:/tmp/.X11-unix' -v /home/ws:/home/ws dudulrx0601/ugv_rpi_ros_humble:ugv_rpi_ros_humble

#sudo xhost +local:docker && docker exec -it UGV_RPI_ROS /bin/bash

#docker restart UGV_RPI_ROS

#docker stop UGV_RPI_ROS

## 로봇 .bashrc 에 편집

alias RHA="sudo xhost +local: &&  sudo docker exec -i -t UGV_RPI_ROS /bin/bash"

alias RHS="sudo docker restart UGV_RPI_ROS"

## 로봇 .bashrc 실행

source .bashrc



### 2. 도커 Attach 전에 필수

### 3.  xhost +

### 4.  echo $DISPLAY

![image](https://github.com/user-attachments/assets/06b087a6-38c0-44ba-b5a4-617c2143281b)


### 5. 2번 터미널에서 도커 스타트

# 로봇 컨테이너 시작

RHS

RHA

### 6.  도커 Attach 

RHA

![image](https://github.com/user-attachments/assets/cd058db1-1302-4651-a8e2-0907674880f5)


### 7. 도커 쉘에서 echo $DISPLAY

### 8. 도커 쉘에서 export $DISPLAY=[4번에서 출력되 화면번호]

export DISPLAY=:1

### 9. 도커에서 화면이 잘 나오는지 테스트

cd senfu/testapp

python3 opencvtest.py

![image](https://github.com/user-attachments/assets/b33e2432-c596-4afc-854c-8002de57af6b)

![image](https://github.com/user-attachments/assets/5ce096eb-526b-448a-ab69-c52779eda3ca)

enter 키를 눌러서 화면을 꺼주세요




