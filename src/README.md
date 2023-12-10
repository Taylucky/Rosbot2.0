# ROSbot Dataset Collection

This is a ROS workspace for collecting a dataset by driving around using the Husarion ROSbot 2.0 using bluetooth controller.


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

#Running the data collection script

Open the terminal and run the following commands
```
cd <path_to_data_collection_launch>
roslaunch data_collection data_collector.launch dest:=$(pwd)/dataset
```

