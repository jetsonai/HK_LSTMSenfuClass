# 환경 설치

## 터보vnc 다운받아서 설치

https://cyfuture.dl.sourceforge.net/project/turbovnc/3.1/TurboVNC-3.1-x64.exe

### 1. turbovnc 접속

### 2. 터미널 아이콘 눌러서 창 2개 열기

![image](https://github.com/user-attachments/assets/2fb09f56-4191-472b-a85c-dce99cb7448a)

### 3. 1번 터미널에서 xhost +

### 4. 1번 터미널에서 echo $DISPLAY

![image](https://github.com/user-attachments/assets/06b087a6-38c0-44ba-b5a4-617c2143281b)


### 5. 2번 터미널에서 도커 스타트

### 6. 2번 터미널에서 DOCKER EXEC 를 하여 도커 쉘접속 

![image](https://github.com/user-attachments/assets/cd058db1-1302-4651-a8e2-0907674880f5)


### 7. 2번 터미널 도커 쉘에서 echo $DISPLAY

### 8. 2번 터미널 도커 쉘에서 export $DISPLAY=[4번에서 출력되 화면번호]

### 9. 2번 도커 터미널에서 rviz2

