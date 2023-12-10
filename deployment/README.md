# Algorithm:
The rosbot_ml.py file is the main script for the autonomous navigation of the rosbot, which deploys the trained ML model onto the rosbot.
The main purpose is to include both lidar and images in our system, so there are 2 parts in the code that is the lidar and the ml model. 
When the minimum distance between the object and rosbot is less than 40 cm, the lidar code runs which will stop the rosbot. Otherwise, the ml model runs which predicts the angular velocity and publishes that to the robot.

# Working:
Copy the rosbot_ml.py file in the src file of husarion_ros.

First, launch the rosbot driver to run all the drivers of the rosbot. :

```
roslaunch husarion_ros rosbot_drivers.launch
```

In the second terminal, run the the rosbot_ml python script for the autonomous navigation.


```
rosrun datacoll rosbot_ml.py
```
Now the robot should be able to navigate and should not crash into any objects.

# Results and Troubleshooting
The process of model training and deploying was done multiple times with different datasets.
During first cycle, the dataset included only straight paths, so our model did not work well in curves.
During the second cycle, the dataset included straight paths and curves. But our model had the issue of running into the wall.
During the third cycle, we trained our model, on zig zag paths, straight path and curves. This 
