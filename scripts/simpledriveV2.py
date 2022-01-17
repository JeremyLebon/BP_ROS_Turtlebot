#! /usr/bin/env python

# import

import rospy
import time
from geometry_msgs.msg import Twist

global forward, turn, Move, Left, Right, Stop

Move = "Move"
Left = "Left"
Right = "Right"
Stop = "Stop"
path= [Move,Left,Move,Left,Move,Left,Move,Left,Stop]
#
def main():
	
	print("test1")
	rospy.init_node("SpeedTest")	#maken van de node
	rate = rospy.Rate(10) #10hz
	#move = Twist() #defining the way we can allocate de values
	pub = rospy.Publisher('cmd_vel', Twist , queue_size=1) #verzenden van het bericht
	index = 0
	print (path)
	
	#De waarden van de move.linear.x mogen niet hoger zijn dan 0,23

	while not rospy.is_shutdown():
        			
		move, timemovement = movement(path[index])
		time.sleep(1)
		pub.publish(move)
		time.sleep(timemovement)
		index +=1
		if len(path) == index:
			exit()

	
def movement(nr):
	moveStep = Twist()
	timeStep = 0
	if nr == Stop :
		moveStep.linear.x = 0.0
		moveStep.angular.z = 0.0
		timeStep = 2

	if nr == Left : 
		moveStep.linear.x = 0.0
		moveStep.angular.z = 0.8
		timeStep = 1

	if nr == Right : 
		moveStep.linear.x = 0.0
		moveStep.angular.z = -0.8
		timeStep = 1

	if nr == Move :
		moveStep.linear.x = 0.1
		moveStep.angular.z = 0.0
		timeStep = 2

	print(nr, " ", moveStep)
	return moveStep, timeStep

  

if __name__ == '__main__':
		main()
		
