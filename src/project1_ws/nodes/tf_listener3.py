#!/usr/bin/env python  
import roslib
roslib.load_manifest('project1_ws')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf_listener3')

    listener = tf.TransformListener()

    # spawn
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(1, 10, 0, 'turtle3')
    
    # velocity
    turtle_vel = rospy.Publisher('turtle3/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/turtle3', '/turtle1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        if not (math.sqrt(trans[0] ** 2 + trans[1] ** 2))<0.1:
            angular = 0.7 * math.atan2(trans[1], trans[0])
            linear = 0.1 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
            cmd = geometry_msgs.msg.Twist()
            cmd.linear.x = linear
            cmd.angular.z = angular
            turtle_vel.publish(cmd)
        else:
            rospy.loginfo("Turtle 3 caught Turtle 1")
            rospy.signal_shutdown("Turtle 3 completed mission.")

        rate.sleep()
