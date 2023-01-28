#!/usr/bin/env python  
import roslib
roslib.load_manifest('project1_ws')
import rospy
import time
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('target2')

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(5, 5, 0, 'turtle1b')
    turtle_vel = rospy.Publisher('turtle1b/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        

        rate.sleep()
