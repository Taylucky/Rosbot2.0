# ROSbot Dataset Collection

This is a ROS workspace for collecting a dataset by driving around using the Husarion ROSbot 2.0 using Bluetooth controller.


# Connecting Bluetooth Controller

Install bluez

```
sudo apt install bluez
```




Put the bluetooth controller in pair mode and run the following commands
```
sudo service bluetooth start
bluetoothctl scan on
pair <your-controller-MAC>
connect <your-controller-MAC>
```

Once the connection is successful, the controller LED light will glow continuously.

# Running the data collection script

Open the terminal and run the following commands
```
cd <path_to_data_collection_launch>
roslaunch data_collection data_collector.launch dest:=$(pwd)/dataset
```


# Results


DATASET: 
The model is working on 8497 data points in total.

TRAINING DATASET: The training dataset contains 6797 data points. The data set is categorized into the following categories. 2650 data points were collected by driving the robot in a straight lap around the hallway. 4148 data points were collected by driving the robot in a zig-zag lap around the hallway.

TESTING DATASET: The testing dataset was obtained by driving the robot around the hallway and randomly selecting 1700 data points from the obtained dataset.

