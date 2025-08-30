# HK_LSTMSenfuClass


Xterm 을 다운받아서 압축을 풀어주세요.

https://files.waveshare.com/wiki/UGV%20Rover%20PT%20ROS2/MobaXterm_Portable_v22.0.zip

![image](https://github.com/user-attachments/assets/9fe633b8-1e5f-41be-b5dd-82e5fe536ede)

압축 해제된 폴더에서 Xterm 실행파일을 실행시켜주세요.

화면의 메뉴에서 Session 아이콘을 클릭해주세요
![image](https://github.com/user-attachments/assets/747d1d00-6781-4fc6-bf9c-c2d95d722f0c)

session 세팅 탕에서 SSH 아이콘을 클릭해주세요.
![image](https://github.com/user-attachments/assets/a968a228-ac43-4827-94f6-4bbc48d8e495)

remote host 입력칸에 192.168.0.10 을 입력하고 OK 해주세요.
![image](https://github.com/user-attachments/assets/50c0497c-181d-40ae-89c6-a1e071dc1b20)

터미널 창에 열리면 아이디 비번 ws / ws 입력해주시면 됩니다.



docker stop ugv_rpi_ros_humble
docker restart ugv_rpi_ros_humble
docker exec -it ugv_rpi_ros_humble /bin/bash


sudo docker run --privileged --name UGV_RPI_ROS -e DISPLAY=unix$DISPLAY -e='QT_X11_NO_MITSHM=1' -e IS_PERSISTENT=TRUE -e ANONYMIZED_TELEMETRY=TRUE --ipc=host -it -d --net=host -v /dev/snd:/dev/snd --volume='/docker_job:/docker_job' --volume='/tmp/.X11-unix:/tmp/.X11-unix' -v /home/ws:/home/ws dudulrx0601/ugv_rpi_ros_humble:ugv_rpi_ros_humble

sudo xhost +local:docker && 

docker exec -it UGV_RPI_ROS /bin/bash

docker restart UGV_RPI_ROS
docker stop UGV_RPI_ROS


source /opt/ros/humble/setup.bash
# argcomplete for ros2 & colcon
eval "$(register-python-argcomplete3 ros2)"
eval "$(register-python-argcomplete3 colcon)"
source /home/ws/ugv_ws/install/setup.bash
export UGV_MODEL=ugv_beast
export LDLIDAR_MODEL=ld19
source /home/ws/ugv_ws/install/setup.bash


ros2 launch ugv_description display.launch.py use_rviz:=true

