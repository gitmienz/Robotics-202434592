import rclpy
from rclpy.node import Node
from custom_interfaces.srv import MoveRobot
import math


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__('srv_server')

        self.srv = self.create_service(MoveRobot, '/move_robot', self.srv_callback)
        self.get_logger().info('Srv Server Ready.')

    def srv_callback(self, request, response):
        response.result_pose.x = request.current_pose.x + round(request.distance*math.cos(request.current_pose.theta), 1)
        response.result_pose.y = request.current_pose.y + round(request.distance*math.sin(request.current_pose.theta), 1)
       
        
        self.get_logger().info(f'Incoming request\nx: {request.current_pose.x}, y: {request.current_pose.y}, theta: {request.current_pose.theta}')
        self.get_logger().info(f'Sending back response: x: {response.result_pose.x}, y: {response.result_pose.y}')
        
        return response


def main():
    rclpy.init()
    node = AddTwoIntsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
