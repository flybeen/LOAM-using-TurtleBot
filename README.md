
[![Video Label](http://img.youtube.com/vi/v_56GsGXoVQ/0.jpg)](https://youtu.be/v_56GsGXoVQ)






### A-LOAM, LiDAR-카메라 융합, KNN을 이용한 객체 분류 (Ubuntu 20.04, ROS Noetic)

#### 문의 사항: peicai69@naver.com

---

먼저, 이 프로그램이 제작될 수 있었던 것은 아래의 기여자들 덕분입니다:

- **A-LOAM (Modifier: Tong Qin, Shaozu Cao)**  
  [https://github.com/HKUST-Aerial-Robotics/A-LOAM](https://github.com/HKUST-Aerial-Robotics/A-LOAM)

- **LeGO-LOAM (TixiaoShan)**  
  [https://github.com/HKUST-Aerial-Robotics/A-LOAM](https://github.com/RobustFieldAutonomyLab/LeGO-LOAM)

- **Turtlebot3 Velodyne (Tevhit Karsli)**  
  [https://github.com/Tevhit/pcl_velodyne_ws/tree/main/src/turtlebot3_velodyne](https://github.com/Tevhit/pcl_velodyne_ws/tree/main/src/turtlebot3_velodyne)


---

### 프로그램 실행 전 준비 사항

#### Step 1: 종속성 프로그램 설치

아래 링크를 참조하여 설치를 진행하세요:  
[https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start)

다음 명령어를 실행합니다:

```bash
$ sudo apt update
$ sudo apt upgrade
$ wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_noetic.sh
$ chmod 755 ./install_ros_noetic.sh 
$ bash ./install_ros_noetic.sh
```

이후, 아래의 ROS 패키지를 설치하세요:

```bash
$ sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
```

추가로 다음 종속성들을 설치하세요:

```bash
$ sudo apt install ros-noetic-dynamixel-sdk
$ sudo apt install ros-noetic-turtlebot3-msgs
$ sudo apt install ros-noetic-turtlebot3
$ sudo apt install gnome-terminal
$ pip install open3d
```

`.bashrc` 파일을 수정하여 Turtlebot3 모델을 설정하세요:

```bash
export TURTLEBOT3_MODEL=waffle
```
