#! /usr/bin/env python

# import

import rospy
import time
from geometry_msgs.msg import Twist

global forward, turn
forward = 0.2
turn = 0
path= [1,0,2,0,1,0,1,0,2,0,1,0,1,0,1,0]

def main():
	
	print("test1")

	rospy.init_node("SpeedTest")	
	rate = rospy.Rate(10) #10hz
	move = Twist() #defining the way we can allocate de values
	#move.linear.x = forward #allocating the values in x direction - linear
	#move.angular.z = turn #allocating the values in z direction - angular
	pub = rospy.Publisher('cmd_vel', Twist , queue_size=1)
	index =0
	
	#De waarden van de move.linear.x mogen niet hoger zijn dan 0,23

	while not rospy.is_shutdown():
        			
		move, timemovement = movement(path[index])
		pub.publish(move)
		time.sleep(timemovement)
		index +=1

	
def movement(nr):
	moveStep = Twist()
	timeStep = 0
	if nr == 0 :
		moveStep.linear.x = 0.0
		moveStep.angular.z = 0.0
		timeStep = 2
	if nr == 1 :
		moveStep.linear.x = 0.1
		moveStep.angular.z = 0.0
		timeStep = 2
	
	if nr == 2 :
		moveStep.linear.x = 0.0
		moveStep.angular.z = 1
		timeStep = 2
	print(nr, " ", moveStep)
	return moveStep, timeStep

  

if __name__ == '__main__':
		main()
		
