#!/usr/bin/env python  
import roslib
roslib.load_manifest('project1_ws')
import rospy
import random
import time
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('target2')

    # spawn a second target
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(5, 5, 0, 'turtle1b')

    rospy.wait_for_service('turtle1b/set_pen')
    setpen = rospy.ServiceProxy('turtle1b/set_pen', turtlesim.srv.SetPen)
    setpen(0,0,0,0,1) #r g b width on/off


    while not rospy.is_shutdown():
        # teleport to a random position
        x = random.randrange(1,10)
        y = random.randrange(1,10)
        rospy.wait_for_service('turtle1b/teleport_absolute')
        teleport = rospy.ServiceProxy('turtle1b/teleport_absolute', turtlesim.srv.TeleportAbsolute)
        teleport(x, y, 0)
      
        # sleep for 5 seconds before teleporting to a new position
        time.sleep(5)
