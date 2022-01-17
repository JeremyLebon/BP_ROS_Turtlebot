#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def laser_callback(msg):

	#Proces van het uitzoeken hoe de scan werkte

	#print msg #lezen van alle waarden van de LaserScan
	#print len(msg.ranges) #aantal waarden dat de laser uitstuurt
	#print msg.ranges[180] #waarde op plaats 180
	#print 'afstand achter robot ', msg.ranges[0]
	#afstand_voor = msg.ranges[0]
	#afstand_voor1 = msg.ranges[350]
	#afstand_voor2 = msg.ranges[10]
	#print (afstand_voor1,afstand_voor,afstand_voor2)

	range1 = msg.ranges[330:360]
	range2 = msg.ranges[0:30]


	minimum1 = min (x for x in range1 if x != 0.0 )
	minimum2 = min (x for x in range2 if x != 0.0)
	minimum = min (minimum2,minimum1)

	print ("mimimum: ",minimum)
	if minimum < 0.3: #0.5 voor halve meter van de muur, 0.0 voor als de object te ver staat
		print ('stop')
		move.linear.x = 0	
		move.angular.z = 2
	else:
		move.angular.z = 0
		move.linear.x = 0.2
		

rospy.init_node('wall_evading')
laser_sub = rospy.Subscriber('scan', LaserScan, laser_callback) #uitlezen van de scan van LaserScan message
	
rate = rospy.Rate(100) #xxhz
move = Twist() #definieren van variabele om waarden toe te kunnen kennen
move.linear.x = 0.1 #toekennen waarden in x-richting - lineair
move.angular.z = 0 #toekennen waarden in z-richting - hoek
pub = rospy.Publisher('cmd_vel', Twist , queue_size=1) #versturen van bericht 'cmd-vel' in de Twist message


#creeeren van een loop waarin hij de snelheid uitstuurt
while not rospy.is_shutdown():
	pub.publish(move)
	rate.sleep()
else:
	move.angular.z = 0
	move.linear.x = 0


