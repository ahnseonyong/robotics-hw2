cmake_minimum_required(VERSION 2.8.3)
project(common_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  std_msgs
)

 add_message_files(
   FILES
   Topic.msg
 )

 generate_messages(
   DEPENDENCIES
   geometry_msgs   std_msgs
 )


catkin_package(
  CATKIN_DEPENDS geometry_msgs rospy std_msgs
)



