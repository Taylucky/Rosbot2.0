# Algorithm:
The rosbot_ml.py file is the main script for the autonomous navigation of the rosbot, which deploys the trained ML model onto the rosbot.
The main purpose is to include both lidar and images in our system, so there are 2 parts in the code that is the lidar and the ml model. 
When the minimum distance between the object and rosbot is less than 40 cm, the lidar code runs which will stop the rosbot. Otherwise, the ml model runs which predicts the angular velocity and publishes that to the robot.

# Requirements
The main packages required are scipy, pytorch and numpy.
Since the rosbot is a 32bit system, we had to directly download the binaries of the necessary packages with the correct version. 

Follow the below steps:

From the provided link, https://github.com/KumaTea/pytorch-arm/releases/tag/v1.8.0, download the following files.

torch-1.8.0-cp38-cp38-linux_armv7l.whl

torchvision-0.9.0-cp38-cp38-linux_armv7l.whl

Copy the below files, to this path /home/husarion/husarion_ws/src/datacoll/src

Open the terminal and run the below commands to install torch and torchvision.

```
cd /home/husarion/husarion_ws/src/datacoll/src
pip install torch-1.8.0-cp38-cp38-linux_armv7l.whl
pip install torchvision-0.9.0-cp38-cp38-linux_armv7l.whl
pip install scipy==1.6
pip install numpy==1.24
```
Run the following the commands to check if the packages are installed

```
pip show torch
pip show torchvision
pip show numpy
pip show scipy
```


# Working:
Copy the rosbot_ml.py and inference.py file in the src file of husarion_ros.

First, launch the rosbot driver to run all the drivers of the rosbot. :

```
roslaunch husarion_ros rosbot_drivers.launch
```

In the second terminal, run the the rosbot_ml python script for the autonomous navigation. 
rosbot_ml is just based on camera.


```
rosrun datacoll rosbot_ml.py
```
rosbot_ml_v3 is based on both camera and lidar.
```
rosrun datacoll rosbot_ml_v3.py
```
Now the robot should be able to navigate and should not crash into any objects.

# Results and Troubleshooting
The process of model training and deploying was done multiple times with different datasets.
During first cycle, the dataset included only straight paths, so our model did not work well in curves.
During the second cycle, the dataset included straight paths and curves. But our model had the issue of running into the wall.
During the third cycle, we trained our model, on zig zag paths, straight path and curves. This 
