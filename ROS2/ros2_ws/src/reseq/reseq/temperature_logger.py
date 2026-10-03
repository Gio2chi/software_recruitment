import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

# Define the TemperatureLogger node
class TemperatureLogger(Node):
    def __init__(self, log_file):
        super().__init__('temperature_logger')
        self.log_file = log_file
        self.subscription = self.create_subscription(
            Float32,
            '/temperature',
            self.temperature_callback,
            10
        )
        self.get_logger().info(f'TemperatureLogger node started, logging to {self.log_file}')

    def temperature_callback(self, msg):
        temperature = msg.data
        self.get_logger().info(f'Received temperature: {temperature}')
        with open(self.log_file, 'a') as f:
            f.write(f'{temperature}\n')

def main(args=None):
    rclpy.init(args=args)

    logger = TemperatureLogger("log.txt")

    rclpy.spin(logger)

    logger.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
