#!/usr/bin/env
import rospy
from std_msgs.msg import Bool

def callback(data):
    rospy.loginfo("RECEIVED DATA: %s", data.data)
    
def listener():
    rospy.init_node("subscriber_node", anonymous = True)
    rospy.Subscriber("interaction", Bool, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
