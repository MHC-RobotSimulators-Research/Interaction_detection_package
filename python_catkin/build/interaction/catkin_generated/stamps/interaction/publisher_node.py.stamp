#!/usr/bin/env
import threading
import rospy
from std_msgs.msg import Bool
from pyInteraction import pyInteraction  

def talk_to_me(checkInteraction):
    pub = rospy.Publisher('interaction', Bool, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1000)
    rospy.loginfo("Publisher Node Started, now publishing msg")
    while not rospy.is_shutdown():
        pub.publish(checkInteraction.getInteract())
        rate.sleep()

if __name__ == "__main__":
    try:
        checkInteraction = pyInteraction()
        talk_to_me(checkInteraction)
    except rospy.ROSInterruptException:
        pass


