# Rosbot2.0

[Autonomous Rosbot Navigation Tutorial ](https://github.com/MissMeriel/ROSbot_data_collection/tree/master)

This repo implemented the entire machine learning pipeline in a real system, deploying the machine learning model onto a ROSbot robot car. This enables the robot to autonomously navigate without colliding with any obstacles.


About Rosbot 2.0


The ROSbot 2.0 is a mobile robot platform developed by Husarion, designed to work seamlessly with the Robot Operating System (ROS). ROS is an open-source middleware framework widely used in robotics research and development. 

ASUS Tinker Board 2GB RAM, 32 GB MicroSD 
RPLIDAR A2 laser scanner with 8m range 
RGBD Camera with image size 640x480 

Installation Steps: 

The rosbot 2.0 had melodic ros version which only supports Python 2. 
To use pytorch model, we decided to upgrade the Ros OS to noetic. The below link was used to flash the OS and upgrade it. 
https://husarion.com/manuals/rosbot/operating-system-reinstallation/ 

Upgraded Software:
Python2--> Python3
Ubuntu 20.04--> Ubuntu 22.04
Ros Melodic --> Ros Noetic


DATASET: 
The model is working on 8497 datapoints in total.

TRAINING DATASET: The training dataset contains 6797 data points. The data set is categorized into following categories. 2650 data points collected by driving the robot in a straight lap around the hallway. 4148 data points collected by driving the robot in a zig zag lap around the hallway.

TESTING DATASET: Testing dataset was obtained by driving the robot around the hallway and randomly selecting 1700 data points from the obtained dataset.

 
