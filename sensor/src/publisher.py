#!/usr/bin/env python
import rospy
from common_msgs.msg import Topic

rospy.init_node('triangle_publisher', anonymous=True)

msg = Topic()

pub = rospy.Publisher("flex", Topic, queue_size = 1)
rate = rospy.Rate(1)
msg.number.data = 0
msg.triangle.x = 0.0
msg.triangle.y = 0.0
msg.triangle.theta = 0.0

while not rospy.is_shutdown():
    msg.number.data += 1
    msg.triangle.x += 0.1
    msg.triangle.y += 0.1
    msg.triangle.theta += 0.01
    pub.publish(msg)
    print("x : ", msg.triangle.x)
    print("y : ", msg.triangle.y)
    print("theta : ", msg.triangle.theta)
    rate.sleep()
