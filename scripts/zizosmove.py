#!/usr/bin/env python
# license removed for brevity
import rospy
import time
from sensor_msgs.msg import JointState
from std_msgs.msg import Float32MultiArray

def state():
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rospy.init_node('python_script', anonymous=False)
    rate = rospy.Rate(100) # 10hz
    home_pos = [0.0 , 0.0 , 0.0]
    desired_pos = [ 2.0 , 1.7 , -0.1] 
    desired_pos2 = [-2.0 , -1.7 , +0.1]
    desired_pos3 = [0.5 , -0.5 , 0.0 ] 
    i = 0.01

    joints = JointState()
                    ## Initial Position ## 
    joints.header.stamp = rospy.Time.now()
    joints.name = ["j0","j1","j2"]
    joints.position = [0.01 , 0.01 , 0.01]
    current = joints.position
    #rospy.loginfo(joints)
    pub.publish(joints)
    # rate.sleep()

    while not rospy.is_shutdown():

        usr0= input("\n*********************\n@@@ How would you like to see the robot moving? \n (1) Assign it specified positions \n (2) pre-determined positions ")
   
                                    ### ASSigning Specified positions ###

        if usr0 == 1:
            j0 = input("\n*********************\nJoint 0 Value: ")
            j1 = input("Joint 1 Value: ")
            j2 = input("Joint 2 Value: ")
            while [round(current[0],2),round(current[1],2),round(current[2],2)] != [j0,j1,j2]:
                joints.header.stamp = rospy.Time.now()
                joints.name = ["j0","j1","j2"]
                joints.position = [ current[0]-((current[0]-j0)*i) , current[1]-((current[1]-j1)*i) , current[2]-((current[2]-j2)*i) ] 
                current = joints.position
                pub.publish(joints)
                rate.sleep()

                                    ### Pre-determined positions ###

        if usr0 == 2:
            usr = input("\n@@@ Move Robot to Position [ 0 / 1 / 2 / 3 ] ")

            if usr == 0:
                                    ### Home POSITION ###

                while [round(current[0],2),round(current[1],2),round(current[2],2)] != home_pos:
                    joints.header.stamp = rospy.Time.now()
                    joints.name = ["j0","j1","j2"]
                    joints.position = [ current[0]-((current[0]-home_pos[0])*i) , current[1]-((current[1]-home_pos[1])*i) , current[2]-((current[2]-home_pos[2])*i) ] 
                    current = joints.position
                    pub.publish(joints)
                    print current,home_pos
                    rate.sleep()
                                    ### POSITION 1 ###

            if usr == 1:
                while [round(current[0],2),round(current[1],2),round(current[2],2)] != desired_pos:
                    joints.header.stamp = rospy.Time.now()
                    joints.name = ["j0","j1","j2"]
                    joints.position = [ current[0]-((current[0]-desired_pos[0])*i) , current[1]-((current[1]-desired_pos[1])*i) , current[2]-((current[2]-desired_pos[2])*i) ] 
                    current = joints.position
                    pub.publish(joints)
                    print current,desired_pos
                    rate.sleep()
                                    ### POSITION 2 ###

            elif usr == 2:
                while [round(current[0],2),round(current[1],2),round(current[2],2)] != desired_pos2:
                    joints.header.stamp = rospy.Time.now()
                    joints.name = ["j0","j1","j2"]
                    joints.position = [ current[0]-((current[0]-desired_pos2[0])*i) , current[1]-((current[1]-desired_pos2[1])*i) , current[2]-((current[2]-desired_pos2[2])*i) ] 
                    current = joints.position
                    pub.publish(joints)
                    print current,desired_pos2
                    rate.sleep()

                                    ### POSITION 3 ###
            elif usr == 3:
                while [round(current[0],2),round(current[1],2),round(current[2],2)] != desired_pos3:
                    joints.header.stamp = rospy.Time.now()
                    joints.name = ["j0","j1","j2"]
                    joints.position = [ current[0]-((current[0]-desired_pos3[0])*i) , current[1]-((current[1]-desired_pos3[1])*i) , current[2]-((current[2]-desired_pos3[2])*i) ] 
                    current = joints.position
                    pub.publish(joints)
                    print current,desired_pos3
                    rate.sleep()

            else:
                print ("Invalid Position")

        
if __name__ == '__main__':
    #state()
    try:
        state()
    except rospy.ROSInterruptException:
        pass
