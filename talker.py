#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    pub2 = rospy.Publisher('chattertwo', Int8, queue_size=10)
    num = 1
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        num = num + 1
        rospy.loginfo(hello_str)
        rospy.loginfo(num)
        pub.publish(hello_str)
        pub2.publish(num)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
