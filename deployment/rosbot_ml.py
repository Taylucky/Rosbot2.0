import rclpy
from rclpy.node import Node
from inference import *
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

import numpy as np


class RosbotML(Node):
    def __init__(self):
        super().__init__('rosbot_ml')
        self.model = load_model('model_cpt\model-20231127_150950-fixnoise-DAVE2v3-336x188-lr0.0001-100epoch-64batch-lossMSE-1Ksamples-INDUSTRIALandHIROCHIandUTAH-noiseflipblur-best.pt')
        self.image = None

        self.create_subscription(Image, 'camera/image_raw', self.image_callback, 1)
        # create publisher for cmd_vel
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 1)

        # create timer for self.run
        self.timer = self.create_timer(0.1, self.run)



    def image_callback(self, msg):
        self.image = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)

    def run(self):
        while True:
            if self.image is not None:
                prediction = inference(self.model, self.image)
                print(prediction)
                # publish prediction
                msg = Twist()
                msg.linear.x = 0.5
                msg.angular.z = prediction[0]
                self.cmd_vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    rosbot_ml = RosbotML()

    rclpy.spin(rosbot_ml)

    rosbot_ml.destroy_node()
    rclpy.shutdown()
                

if __name__ == '__main__':
    main()