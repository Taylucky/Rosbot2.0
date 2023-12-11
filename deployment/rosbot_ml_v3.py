#!/usr/bin/env python3
import rospy
#from rospy.node import Node
from inference import *
import cv2
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import numpy as np


class RosbotML:
    def __init__(self):
        rospy.init_node('rosbot_ml')
        self.model=torch.load('/home/husarion/husarion_ws/src/datacoll/src/best_model2.pt',map_location=torch.device('cpu'))
        #self.model = load_model('model-fixnoise-DAVE2v3-135x240-lr0.0001-100epoch-64batch-lossMSE-3Ksamples-INDUSTRIALandHIROCHIandUTAH-noiseflipblur-best.pt')
        self.image = None
        self.bridge=CvBridge()
        self.image_sub=rospy.Subscriber("/camera/rgb/image_rect_color", Image, self.image_callback, queue_size=1)
        # create publisher for cmd_vel
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

        # create timer for self.run
        rospy.Timer(rospy.Duration(0.1), self.run)
        rospy.Subscriber('/scan', LaserScan, self.lidar_callback)
        self.distance_threshold = 0.3
        self.distances= [0.8]*1
        self.min_distance=0.8

       # self.twist_msg = Twist()

    # def image_callback(self, msg):
    #     self.image = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        self.image = cv2.resize(cv_image,(640,480))


    def lidar_callback(self, scan_msg):
        # Extract the distances from the LiDAR scan
        self.distances = scan_msg.ranges

        # Check the minimum distance
        self.min_distance = min(self.distances)

        # Print the minimum distance for debugging
        rospy.loginfo("Min Distance: {:.2f} meters".format(self.min_distance))

    # def run(self):
    #     while True:
    #         if self.image is not None:
    #             prediction = inference(self.model, self.image)
    #             print(prediction)
    #             # publish prediction
    #             msg = Twist()
    #             msg.linear.x = 0.5
    #             msg.angular.z = prediction[0]
    #             self.cmd_vel_pub.publish(msg)

    def run(self, event):
        #distances= scan_msg.ranges
        self.min_distance = min(self.distances)
        rospy.loginfo("Min Distance: {:.2f} meters".format(self.min_distance))
        if self.image is not None:
           if self.min_distance < self.distance_threshold:
              rospy.loginfo("Stopping the robot!")
             # self.twist_msg.linear.x = 0.0
              msg = Twist()
              msg.linear.x = 0.0
              self.cmd_vel_pub.publish(msg)
           else:
              prediction = inference(self.model, self.image) 
              print(prediction)
            # publish prediction
              msg = Twist()
              msg.linear.x = 0.2
              msg.angular.z = prediction[0]
              print(msg.angular.z)
              self.cmd_vel_pub.publish(msg)

def main(args=None):
    # rclpy.init(args=args)
    #
    # rosbot_ml = RosbotML()
    #
    # rclpy.spin(rosbot_ml)
    rosbot_ml = RosbotML()
    rospy.spin()

    #rosbot_ml.destroy_node()
    #rclpy.shutdown()
                

if __name__ == '__main__':
    main()
