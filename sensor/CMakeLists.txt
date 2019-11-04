cmake_minimum_required(VERSION 2.8.3)
project(sensor)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  std_msgs
  common_msgs
)

catkin_package(
  CATKIN_DEPENDS geometry_msgs rospy std_msgs
)


