#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

#lijst van mogelijke doelen waaruit de gebruiker kan kiezen
Kamer_1 = "Kamer 1"
Kamer_2 = "Kamer 2"
Kamer_3 = "Kamer 3"
Kamer_4 = "Kamer 4"
Kamer_5 = "Kamer 5"
Kamer_6 = "Kamer 6"
#andere variabelen declareren
path = []
GO = "GO"
x = "counter"
#creeeren van een loop om een traject te vragen aan de gebruiker
while x != GO:
    try:
        x = input("Geef Kamer_X in, GO voor te starten: ")
        path.append(x)
    except NameError:
        print ("Deze kamer bestaat niet, probeer opnieuw!")
    print(path) #controle

#functie om de doelen te verzenden
def movebase_client():
    index = 0
    while not rospy.is_shutdown():
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()
        goal = traject(path[index])
        index += 1
        client.send_goal(goal)
        wait = client.wait_for_result()
        if len(path) == index:
            print ("All Goals Reached!")
            exit()

#locaties van de verschillende kamers op de kaart van Rviz
def traject(kamer):
    goal = MoveBaseGoal() #gebruik maken van bestaande message file in ROS
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    if kamer == Kamer_1:
        goal.target_pose.pose.position.x = 5
        goal.target_pose.pose.position.y = 2
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_2:
        goal.target_pose.pose.position.x = 6
        goal.target_pose.pose.position.y = -2
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_3:
        goal.target_pose.pose.position.x = 1
        goal.target_pose.pose.position.y = 3
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_4:
        goal.target_pose.pose.position.x = -3
        goal.target_pose.pose.position.y = 2
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_5:
        goal.target_pose.pose.position.x = -6
        goal.target_pose.pose.position.y = 3
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_6:
        goal.target_pose.pose.position.x = -7
        goal.target_pose.pose.position.y = -3
        goal.target_pose.pose.orientation.w = 1.0

    print(kamer, goal)
    return goal #resultaat van de functie 'traject'


if __name__ == '__main__':
    try:
        rospy.init_node('SimpleGoalV2') #maken van een nieuwe node
        result = movebase_client() #het resultaat van de functie in een veriabele steken
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")


