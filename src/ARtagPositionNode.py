#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from ar_track_alvar_msgs.msg import *

def markers_cb(data):
    for marker in data.markers:
        msg_pose=PoseStamped()
        msg_pose=marker.pose
        pub = rospy.Publisher('msg_pose', move_base_simple/goal, queue_size=10)
        pub.publish(msg_pose)



def artagPositionRecorder():
    rospy.init_node('ArtagPositionRecoder', anonymous=True)
    rospy.Subscriber("/ar_pose_marker",AlvarMarkers,markers_cb)
    rospy.spin()

if __name__=='__main__':
    artagPositionRecorder()
