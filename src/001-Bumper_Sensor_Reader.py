#!/usr/bin/env python
"""Printing out the state og the bumper sensor"""
"""ahmed9998@hotmail.com"""

#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from kobuki_msgs.msg import BumperEvent
from geometry_msgs.msg import Twist # This is the message type the robot uses for velocities

g_bump= None

class BumpReader():
    def __init__(self):
        rospy.loginfo('bumberReactor')
        rospy.init_node('BumpReactorNode')
        self.bumperVal= None
        self.subscribe = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, self.callback)

    def callback(self,data):
        self.bumperVal=data.state

    def run(self):
        rate=rospy.Rate(10)

        # while self.bumperVal is None:
        #     rospy.sleep(.1)

        while not rospy.is_shutdown():
            if self.bumperVal==True:
                print " pressed"
                return True

            else:
                print "not Pressed"
                return False


if __name__ == '__main__':
    bump = BumpReader()
    while not rospy.is_shutdown():

        bumperValue = bump.run()