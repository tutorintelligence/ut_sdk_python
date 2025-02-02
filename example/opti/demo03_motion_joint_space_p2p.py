# Copyright 2021 The UmbraTek Inc. All Rights Reserved.
#
# Software License Agreement (BSD License)
#
# Author: Jimy Zhang <jimy.zhang@umbratek.com> <jimy92@163.com>
# =============================================================================
import sys
import argparse
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from utapi.utra.utra_api_tcp import UtraApiTcp
from common import print_msg

if __name__ == '__main__':
    """This is a demo of movement in joint space 
    """
    parser = argparse.ArgumentParser()
    parser.description = 'ubot demo'
    parser.add_argument("--ip", help=" ", default="127.0.0.1", type=str)
    args = parser.parse_args()

    ubot = UtraApiTcp(args.ip)

    ret = ubot.reset_err()  # Reset error
    print("reset_error   :%d" % (ret))
    # Set the operating mode of the arm, 0: position control mode
    ret = ubot.set_motion_mode(0)
    print("set_motion_mode   :%d" % (ret))
    ret = ubot.set_motion_enable(8, 1)  # Set the enable state of the arm
    print("set_motion_enable :%d" % (ret))
    # Set the running status of the arm, 0: Set to ready
    ret = ubot.set_motion_status(0)
    print("set_motion_status :%d" % (ret))

    joint = [0, 0, 0, 0, 0, 0, 0]
    speed = 0.1
    acc = 3
    ret = ubot.moveto_joint_p2p(joint, speed, acc, 60)

    joint1 = [1.248, 1.416, 1.155, -1.252, -1.248, -0.003, 0.1]
    joint2 = [0.990, 1.363, 1.061, -1.291, -0.990, -0.006, 0.1]
    joint3 = [1.169, 1.022, 1.070, 1.058, -1.169, -0.004, 0.1]
    speed = 0.1
    acc = 3
    ret = ubot.moveto_joint_p2p(joint3, speed, acc, 60)
    print("moveto_joint_p2p   :%d" % (ret))
    ret = ubot.moveto_joint_p2p(joint1, speed, acc, 60)
    print("moveto_joint_p2p   :%d" % (ret))
    ret = ubot.moveto_joint_p2p(joint2, speed, acc, 60)
    print("moveto_joint_p2p   :%d" % (ret))
    ret = ubot.moveto_joint_p2p(joint3, speed, acc, 60)
    print("moveto_joint_p2p   :%d" % (ret))
