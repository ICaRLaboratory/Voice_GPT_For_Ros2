#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class LimoMover(Node):
    def __init__(self):
        super().__init__('limo_mover')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.start_time = time.time()
        self.duration = 800 / 0.5  # 800 meters at 0.5 m/s (adjust speed if needed)
        self.moving = True
        self.timer = self.create_timer(0.1, self.move_limo)

    def move_limo(self):
        if self.moving:
            elapsed_time = time.time() - self.start_time

            if elapsed_time < self.duration:
                msg = Twist()
                msg.linear.x = 0.5  # Set speed to 0.5 meters/second
                msg.angular.z = 0.0  # No rotation, move straight
                self.publisher.publish(msg)
            else:
                self.stop_limo()
    
    def stop_limo(self):
        self.moving = False
        msg = Twist()
        msg.linear.x = 0.0  # Stop movement
        msg.angular.z = 0.0
        self.publisher.publish(msg)
        self.get_logger().info('Limo has moved 800 meters and stopped.')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    limo_mover = LimoMover()
    rclpy.spin(limo_mover)

if __name__ == '__main__':
    main()
