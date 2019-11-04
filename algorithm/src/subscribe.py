#!/usr/bin/env python
import rospy
import math as mt
from common_msgs.msg import Topic

def callback(msg):
    print("triangle")
    print(msg.number.data * msg.triangle.x * msg.triangle.y * mt.sin(msg.triangle.theta) / 2)

    
rospy.init_node("triangle_subscriber")
sub = rospy.Subscriber("flex", Topic, callback)
rospy.spin()
