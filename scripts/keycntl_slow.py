#!/usr/bin/env python
import rospy, time
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

rospy.wait_for_service('/motor_on')
rospy.wait_for_service('/motor_off')
rospy.on_shutdown(rospy.ServiceProxy('/motor_off',Trigger).call)
rospy.ServiceProxy('/motor_on',Trigger).call()

rospy.init_node('keyboard_cmd_vel')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

while not rospy.is_shutdown():
    vel=Twist()
    direction = raw_input('w a s z, return:stop > ')
    if 'w' in direction: vel.linear.x = 0.1
    if 'z' in direction: vel.linear.x = -0.1
    if 'a' in direction: vel.angular.z = 3.14/4  #pi/4[rad/sec]
    if 'd' in direction: vel.angular.z = -3.14/4
    if 'q' in direction: break

    pub.publish(vel)
    time.sleep(1.0)
    vel.linear.x = 0.0
    vel.angular.z = 0.0
    pub.publish(vel)


