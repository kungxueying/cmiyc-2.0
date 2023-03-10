#!/usr/bin/env python  
import roslib
roslib.load_manifest('project1_ws')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf_listener2')

    listener = tf.TransformListener()
    
    # spawn
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(1, 1, 0, 'turtle2')
   
   # velocity
    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    # set pen (change trail color to red)
    rospy.wait_for_service('turtle2/set_pen')
    setpen = rospy.ServiceProxy('turtle2/set_pen', turtlesim.srv.SetPen)
    setpen(255,0,0,2,0) #r g b width on/off

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        if not (math.sqrt(trans[0] ** 2 + trans[1] ** 2))<0.1:
            angular = 0.7 * math.atan2(trans[1], trans[0])
            linear = 0.1 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
            cmd = geometry_msgs.msg.Twist()
            cmd.linear.x = linear*8
            cmd.angular.z = angular*8
            turtle_vel.publish(cmd)
        else:
            rospy.loginfo("Turtle 2 caught Turtle 1")
            rospy.signal_shutdown("Turtle 2 completed mission.")

        rate.sleep()
