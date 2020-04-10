#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8



def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + 'I also heard the number %u', data.data)


def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.Subscriber('chattertwo', Int8, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
