import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int16MultiArray
import numpy as np

now_location = np.array([0,0])


class Processor(Node):

    def __init__(self):
        super().__init__('processor')
        self.subscription_ = self.create_subscription(String, '/demo_topic', self.callback, 10)
        self.subscription_
        self.publisher_ =  self.create_publisher(String, '/processed_topic', 10)
        self.timer = self.create_timer(0.1, self.publish_message)

    def calculate(self):
        if self.subscription_ == 'w':
            now_loaction += np.array([0,1])
        elif self.subscription_ == 'a':
            now_location += np.array([-2, 0])
        elif self.subscription_ == 's':
            now_location += np.array([0,-1])
        elif self.subscription_ == 'd':
            now_location += np.array([1,0])

    def callback(self, msg):
        self.get_logger().info(f'talker : "{msg.data}"')
        self.get_logger().info(f'now location : {now_location}')

    def publish_message(self):
        self.calculate()
        msg = String()
        msg.data = f"now location = {self.calculate}"
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = Processor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()