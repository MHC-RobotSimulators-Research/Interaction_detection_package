# Interaction detection package

## Overview
A hardware module for detecting and differentiating arm interactions in the Raven-II surgical robot platform. This package enables accurate labeling of datasets for training force prediction machine learning models.
Author: Mai Bui (bui23m@mtholyoke.edu)
## Background
Raven-II is a research platform for minimally invasive robotically assisted surgery, developed by the Biorobotics Laboratory at the University of Washington, Seattle¹.

![Screenshot 2024-11-18 at 10 37 55 PM](https://github.com/user-attachments/assets/86c70b14-0580-475d-8ea6-ca7c4a751bcd)

Figure 1: Raven-II surgical robot platform
While the platform offers robust hardware, it lacks haptic feedback—a crucial element in surgeon's decision-making². Various approaches have been proposed to add haptic feedback, with machine learning-based force prediction being one of the most common methods³,⁴. Training these models requires datasets labeled with force or interaction data, but existing labeling methods often struggle to differentiate between robot arms⁵.
## Hardware Requirements
### Arduino Setup

![Screenshot 2024-11-18 at 9 37 14 PM](https://github.com/user-attachments/assets/43ad7e48-0bda-453c-a99d-495ce9cd3be2)

### Conductive Phantom Materials
* Woven copper+nickel plated polyester conductive cloth
* Loctite Clear Silicone Waterproof Sealant

 ![Screenshot 2024-11-18 at 9 36 13 PM](https://github.com/user-attachments/assets/5e157052-6179-45c9-825f-b847e90b65aa)
 
## Software Requirements
### Tested Platform
* Ubuntu 20.04
* Python 3.8
* ROS Noetic
* Arduino Nano
### Dependencies
* <a href="[https://readme.com/](https://github.com/collaborative-robotics/crtk_python_client)" target="_blank">CRTK Python Client</a>
* <a href="[https://readme.com/](https://github.com/collaborative-robotics/crtk_msgs)" target="_blank">CRTK Messages</a>
* <a href="[https://readme.com/](https://github.com/MHC-RobotSimulators-Research/Raven2_Dual_Platform_Controller)" target="_blank">Raven2 Dual Platform Controller</a>
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
