cmake_minimum_required(VERSION 2.8.3)
project(algorithm)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  std_msgs
)


catkin_package(
  CATKIN_DEPENDS geometry_msgs rospy std_msgs math
)


