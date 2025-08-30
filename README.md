# HK_LSTMSenfuClass


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

