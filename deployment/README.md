Algorithm:
The rosbot_ml.py file is the main script for the autonomous navigation of the rosbot, which deploys the trained ML model onto the rosbot.
The main purpose is to include both lidar and images in our system, so there are 2 parts in the code that is the lidar and the ml model. 
When the minimum distance between the object and rosbot is less than 40 cm, the lidar code runs which will stop the rosbot. Otherwise, the ml model runs which predicts the angular velocity and publishes that to the robot.

Working:

First, launch the rosbot driver to run all the drivers of the rosbot. :

```
roslaunch husarion_ros rosbot_drivers.launch
```
