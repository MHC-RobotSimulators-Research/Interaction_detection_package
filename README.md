# Interaction detection package
Author: Mai Bui (bui23m@mtholyoke.edu)

## Description
Raven-II (Fig 1: add an image of Raven-II here) is a research platform for minimally invasive robotically assisted surgery developed by the Biorobotics Laboratory at the University of Washington, Seattle1. While it offers robust hardware, it lacks haptic feedback which plays an important role in surgeon’s decision making2. There have been multiple proposed approaches to add haptic feedback, one of the most common being the use of machine learning models to predict force3,4. Training these models usually requires datasets labeled with force or interaction data. However, some methods of labeling interaction are unable to differentiate between robots arms5.

This study focused on building an arduino based hardware module which detects when an arm is interacting and is capable of differentiating between the robot’s arms. The interaction data will then be used to label datasets for use in training force prediction machine learning models.
## Usage
![Screenshot 2024-11-18 at 7 52 46 PM](https://github.com/user-attachments/assets/a1b7a92a-4d4d-4d5a-ba43-81515cad48f0)
### Tested Platform
Interaction detection package has been tested on Ubuntu 20.04 (Python 3.8 and ROS Noetic) and Arduino Nano
### Dependency
Requires ROS and a couple of ROS modules. Ensure you have ROS1 installed and build the CRTK Python Client, CRTK Messages, Raven 2 modules for <a href="[https://readme.com/](https://github.com/MHC-RobotSimulators-Research/Raven2_Dual_Platform_Controller)" target="_blank">Raven2 Dual Platform Controller</a>
Additionally, you need telematrix, rospy packages. To install it, you can use pip:
```
pip install telemetrix
```
Besides, for Arduino IDE to work, you need to upload Telemetrix4Arduino Sketch by following this instruction from MrYsLab: <a href="https://mryslab.github.io/telemetrix/telemetrix4arduino/" target="_blank">Telemetrix4Arduino</a>
To create the conductive phantom, you need to buy: woven copper+nickle plated polyester conductive cloth, Loctite Clear Silicone Waterproof Sealant.

 ![Screenshot 2024-11-18 at 9 36 13 PM](https://github.com/user-attachments/assets/5e157052-6179-45c9-825f-b847e90b65aa)
 
Arduino Setup:

![Screenshot 2024-11-18 at 9 37 14 PM](https://github.com/user-attachments/assets/43ad7e48-0bda-453c-a99d-495ce9cd3be2)

### Installation
Git clone: 
```
cd ~
git clone https://github.com/https://github.com/MHC-RobotSimulators-Research/Interaction_detection_package.git
```
Build in local catkin workspace:
```
cd catkin_workspace && mkdir build
cd build
cmake ..
make
```
### Launching
Run the script by rosrun command: 
```
rosrun interaction publisher_node
```
