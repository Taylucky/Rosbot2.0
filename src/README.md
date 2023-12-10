# ROSbot Dataset Collection

This is a ROS workspace for collecting a dataset by driving around using the Husarion ROSbot 2.0 using bluetooth controller.


# Connecting Bluetooth Controller

Install bluez
sudo apt install bluez


sudo service bluetooth start
bluetoothctl scan on

Put the bluetooth controller in pair mode and run the following commands
pair <your-controller-MAC>
connect <your-controller-MAC>

Once the connection is successful, the controller led light will glow continuously.

