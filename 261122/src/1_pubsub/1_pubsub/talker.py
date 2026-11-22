import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, '/demo_topic', 10)
        self.start_time = time.time()
        self.timer = self.create_timer(0.1, self.publish_direction)

    def publish_direction(self):
        direction = input("inputd direction (w,a,s,d): ").lower()
        msg = String()
        msg.data = f"Hello ROS2: {direction}"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{direction}"')

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()