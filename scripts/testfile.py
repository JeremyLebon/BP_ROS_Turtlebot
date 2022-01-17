#! /usr/bin/env python

# import

import rospy

list= [1,4,5,1]

som = sum(list)
gemiddelde = som/len(list)

minimum = min(list)


print som, gemiddelde, minimum
