# Catch Me If You Can (Extended version)
This is a school project developed for the Autonomous Robotics course.
I extended the existing Catch Me If You Can game with some new features. 
[Link to original project](https://github.com/jatinarora30/Catch-me-if-you-can-Turtlesim- )

# Description
4 chaser turtles are chasing 2 target turtles in the game, two of them (turtle2 and turtle3) are chasing turtle1, while the other two (turtle4 and turtle5) are chasing turtle1b. Both of the target turtles move by being teleported to a random position every 5 seconds. Once a chaser turtle successfully chases its target turtle, it will stop moving. Turtle2’s speed has been increased and its trail colour is changed to red, while turtle5’s speed has been decreased and its trail colour is changed to green. Both the target turtles have no trail.

# Additional Features
In our extended project, several changes have been made, including:
1. Changed the number of targets from 1 to 2.
2. 2 chasers will chase the 1st target, while another 2 chasers will chase the 2nd target.
3. The two targets move by being teleported to a random position every 5 seconds, rather than being controlled by arrow keys.
4. All 4 chaser turtles’ initial location has been changed (one at each corner of a square) so that the initial game interface looks neater.
5. turtle2’s speed has been increased, turtle5’s speed has been decreased, while the remaining two chasers’ speed are not changed.
6. turtle2’s trail colour is changed to red, while turtle5’s trail colour is changed to green. The remaining two chasers’ trail colour remains the same, which is white.
7. Both targets do not have trails.
8. The status of the turtles are being printed onto the console. For example, “Turtle 2 caught Turtle 1”.
9. A few bugs in the original project are fixed. For example, rospy.signal_shutdown() needs to take one argument when it is being called. However, no argument is taken by rospy.signal_shutdown() functions in the original project, which causes error messages being printed on the console when a certain process is killed. This problem is fixed in our project.

# Method to Launch
After cloning this project to your local site, use the below command to launch the game:
```
roslaunch project1_ws final.launch
```
