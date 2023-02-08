#!/usr/bin/env python  
import roslib
roslib.load_manifest('project1_ws')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf_listener5')

    listener = tf.TransformListener()

    # spawn
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(10, 10, 0, 'turtle5')
    
    # velocity
    turtle_vel = rospy.Publisher('turtle5/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    # set pen (change trail color to green)
    rospy.wait_for_service('turtle5/set_pen')
    setpen = rospy.ServiceProxy('turtle5/set_pen', turtlesim.srv.SetPen)
    setpen(0,255,0,2,0) #r g b width on/off

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/turtle5', '/turtle1b', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        if not (math.sqrt(trans[0] ** 2 + trans[1] ** 2))<0.1:
            angular = 0.7 * math.atan2(trans[1], trans[0])
            linear = 0.1 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
            cmd = geometry_msgs.msg.Twist()
            cmd.linear.x = linear*0.05
            cmd.angular.z = angular*0.05
            turtle_vel.publish(cmd)
        else:
            rospy.loginfo("Turtle 5 caught Turtle 1b")
            rospy.signal_shutdown("Turtle 5 completed mission.")


        rate.sleep()
