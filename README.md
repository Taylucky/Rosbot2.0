# Rosbot2.0

[Autonomous Rosbot Navigation Tutorial ](https://github.com/MissMeriel/ROSbot_data_collection/tree/master)

This repo implemented the entire machine learning pipeline in a real system, deploying the machine learning model onto a ROSbot robot car. This enables the robot to autonomously navigate without colliding with any obstacles.


About Rosbot 2.0


The ROSbot 2.0 is a mobile robot platform developed by Husarion, designed to work seamlessly with the Robot Operating System (ROS). ROS is an open-source middleware framework widely used in robotics research and development. 

ASUS Tinker Board 2GB RAM, 32 GB MicroSD 
RPLIDAR A2 laser scanner with 8m range 
RGBD Camera with image size 640x480 
![image](https://github.com/Taylucky/Rosbot2.0/blob/master/figures/IMG_2994.jpg)

Installation Steps: 

The rosbot 2.0 had melodic ros version which only supports Python 2. 
To use pytorch model, we decided to upgrade the Ros OS to noetic. The below link was used to flash the OS and upgrade it. 
https://husarion.com/manuals/rosbot/operating-system-reinstallation/ 

Upgraded Software:
Python2--> Python3
Ubuntu 20.04--> Ubuntu 22.04
Ros Melodic --> Ros Noetic


# Starting Rosbot

To set up wifi and connect to monitor and mouse, follow the referencer here. https://husarion.com/tutorials/howtostart/rosbot---quick-start/#connecting-rosbot-to-your-wi-fi-network.

Copy start_rosbot.sh to /home/husarion.

Run this cmnd chmod +x start_rosbot.sh to give it executable permissions.

Run ./start_rosbot.sh on the terminal.

In the end, rosbot can navigate automatically in the building like the vedio.<br>
(https://github.com/Taylucky/Rosbot2.0/assets/61022721/c4c62644-ddf7-4cfc-8db3-5d676099ecea)
 
