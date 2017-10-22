#!/usr/bin/env python
# Had Help from """https://github.com/LCAS/teaching/wiki/First-Turtlebot-coding"""
#"""Modify the variables linearSpeed and angularSpeed as needed"""

import rospy
#import numpy as np
from geometry_msgs.msg import Twist # This is the message type the robot uses for velocities


class CommandVelocity():
    """Driving my robot
    """

    def __init__(self):
        rospy.loginfo("Starting node")
        self.pub = rospy.Publisher("/cmd_vel_mux/input/navi", Twist) # Creating a publisher with whatever name...

    # A function to send velocities until the node is killed
    def send_velocities(self,linearSpeed=[], angularSpeed=[]):
        r = rospy.Rate(10) # Setting a rate (hz) at which to publish
        while not rospy.is_shutdown(): # Runnin until killed
            rospy.loginfo("Sending commands")
            twist_msg = Twist() # Creating a new message to send to the robot
            twist_msg.linear.x=linearSpeed[0]
            twist_msg.linear.y = linearSpeed[1]
            twist_msg.linear.z = linearSpeed[2]

            twist_msg.angular.x= angularSpeed[0]
            twist_msg.angular.y = angularSpeed[1]
            twist_msg.angular.z = angularSpeed[2]
            # ... put something relevant into your message

            self.pub.publish(twist_msg) # Sending the message via our publisher
            r.sleep() # Calling sleep to ensure the rate we set above



if __name__ == '__main__':
    rospy.init_node("command_velocity")
    cv = CommandVelocity()
    linearSpeed=[0.0,0.0,0.0]
    angularSpeed=[0.0,0.0,0.5]
    cv.send_velocities(linearSpeed,angularSpeed) # Calling the function
    rospy.spin()
