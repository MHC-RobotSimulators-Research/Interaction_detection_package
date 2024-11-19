# Interaction detection package

## Overview
A hardware module for detecting and differentiating arm interactions in the Raven-II surgical robot platform. This package enables accurate labeling of datasets for training force prediction machine learning models.
Author: Mai Bui (bui23m@mtholyoke.edu)
## Background
Raven-II is a research platform for minimally invasive robotically assisted surgery, developed by the Biorobotics Laboratory at the University of Washington, Seattle.

![Screenshot 2024-11-18 at 10 37 55 PM](https://github.com/user-attachments/assets/86c70b14-0580-475d-8ea6-ca7c4a751bcd)

Figure 1: Raven-II surgical robot platform
An Arduino-based hardware solution that addresses a critical challenge in surgical robotics: accurate labeling of robot-tissue interaction datasets. By detecting and differentiating between arm interactions in the Raven-II surgical robot platform, this package solves the problem of creating accurately labeled datasets for:

* Training force prediction models to develop haptic feedback systems
* Validating robot-tissue interaction detection

### Key Features:

* Real-time interaction detection
* Distinct identification of individual robot arms
* Automated dataset labeling
* Integration with ROS ecosystem

### System workflow

![Screenshot 2024-11-18 at 7 52 46 PM](https://github.com/user-attachments/assets/73ef2092-11c9-4b7b-8c51-71446af26d10)

## Hardware Requirements
### Arduino Setup

<img src="https://github.com/user-attachments/assets/43ad7e48-0bda-453c-a99d-495ce9cd3be2" width="500" alt="Arduino Setup" />

### Conductive Phantom Materials
* Woven copper+nickel plated polyester conductive cloth
* Loctite Clear Silicone Waterproof Sealant

<img src="https://github.com/user-attachments/assets/5e157052-6179-45c9-825f-b847e90b65aa" width="500" alt="Conductive Phantom" />

## Software Requirements
### Tested Platform
* Ubuntu 20.04
* Python 3.8
* ROS Noetic
* Arduino Nano
### Dependencies   
* [CRTK Python Client](https://github.com/collaborative-robotics/crtk_python_client)

* [CRTK Messages](https://github.com/collaborative-robotics/crtk_msgs)

* [Raven2 Dual Platform Controller](https://github.com/MHC-RobotSimulators-Research/Raven2_Dual_Platform_Controller)
* rospy
### Arduino 
* telematrix
~~~
pip install telemetrix
~~~
* Upload Telemetrix4Arduino to Arduino IDE by following this instruction from MrYsLab: <a href="https://mryslab.github.io/telemetrix/telemetrix4arduino/" target="_blank">Telemetrix4Arduino</a>

## Installation
Clone the Repository
~~~
cd ~
git clone https://github.com/https://github.com/MHC-RobotSimulators-Research/Interaction_detection_package.git
~~~
Build in your local catkin workspace:
~~~
cd catkin_workspace && mkdir build
cd build
cmake ..
make
~~~
### Launching
Launch the interaction detection node:
~~~
rosrun interaction publisher_node
~~~
