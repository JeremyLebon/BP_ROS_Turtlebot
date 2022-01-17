#! /usr/bin/env python

# import

import rospy
import time
from geometry_msgs.msg import Twist

global forward, turn
forward = 0.2
turn = 0

def main():
	
	print("test1")

	rospy.init_node("SpeedTest")	
	rate = rospy.Rate(10) #10hz
	move = Twist() #defining the way we can allocate de values
	move.linear.x = forward #allocating the values in x direction - linear
	move.angular.z = turn #allocating the values in z direction - angular
	pub = rospy.Publisher('cmd_vel', Twist , queue_size=1)

	
	#De waarden van de move.linear.x mogen niet hoger zijn dan 0,23

	while not rospy.is_shutdown():
        	
		#rijden()
		move.linear.x  = 0
		move.angular.z = 1
		time.sleep(2)
		pub.publish(move)
		move.linear.x  = 0
		time.sleep(2)
		pub.publish(move)
		
		time.sleep(2)
		pub.publish(move)
		move.angular.z = 0 
		rate.sleep()
		

	
def rijden():

	print("test2")
	forward = 0.1
	time.sleep(2)
	forward = 0
	time.sleep(2)
	turn = 1
	time.sleep(2)
	turn = 0 

	print("test3")

def draaien():

	print("test2")
	forward = 0.1
	time.sleep(2)
	forward = 0
	time.sleep(2)
	turn = 1
	time.sleep(2)
	turn = 0 

	print ("test3")
	
  

if __name__ == '__main__':
		main()
		
