import sys
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('srv_client')
        self.cli = self.create_client(AddTwoInts, '/add_two_ints') #서비스 타입, 이름
        
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
            
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a.my_num = int(a)
        self.req.b.my_num = int(b)
        
        self.future = self.cli.call_async(self.req) #클라이언트가 요청보냄
        rclpy.spin_until_future_complete(self, self.future) #응답 받을때 까지 요청
        
        return self.future.result()


def main():
    rclpy.init()
    client = AddTwoIntsClient()
    response = client.send_request(sys.argv[1], sys.argv[2])
    client.get_logger().info(f'Sum: {response.sum.my_num}')
    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
