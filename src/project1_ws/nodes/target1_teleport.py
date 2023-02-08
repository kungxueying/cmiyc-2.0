#!/usr/bin/env python  
import roslib
roslib.load_manifest('project1_ws')
import rospy
import random
import time
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('target1_teleport')

    while not rospy.is_shutdown():
        # teleport to a random position
        x = random.randrange(1,10)
        y = random.randrange(1,10)
        rospy.wait_for_service('turtle1/teleport_absolute')
        teleport = rospy.ServiceProxy('turtle1/teleport_absolute', turtlesim.srv.TeleportAbsolute)
        teleport(x, y, 0)
      
        # sleep for 5 seconds before teleporting to a new position
        time.sleep(5)
