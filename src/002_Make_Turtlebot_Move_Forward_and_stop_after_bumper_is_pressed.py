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



class GoForward():


    def __init__(self):
        #rospy.init_node('Go_Forward')
        rospy.loginfo('Go_ForwardNode')
        self.pub = rospy.Publisher('/cmd_vel_mux/input/navi',Twist )


    def moveForward(self,linearSpeed):
        r= rospy.Rate(10)  # Setting a rate (hz) at which to publish
        #while not rospy.is_shutdown():  # Runnin until killed
        #    rospy.loginfo("Sending commands")
        twist_msg = Twist()  # Creating a new message to send to the robot
        twist_msg.linear.x = linearSpeed
        self.pub.publish(twist_msg) # Sending the message via our publisher
        r.sleep()  # Calling sleep to ensure the rate we set above



if __name__ == '__main__':
    linearSpeed=0.2
    rospy.loginfo('0.2')
    forward = GoForward()
    bump = BumpReader()
    bumperValue = bump.run()
    rospy.loginfo('Here')
    #-----------------------------------------
    cont=True
    while not rospy.is_shutdown():
        while bumperValue==False: #notpressed

            forward.moveForward(linearSpeed)
            bumperValue = bump.run()
        while bumperValue==True:
            
            bumperValue = bump.run()
            print 'else'
        continue
        rospy.spin()


