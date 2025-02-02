# Copyright 2020 The UmbraTek Inc. All Rights Reserved.
#
# Software License Agreement (BSD License)
#
# Author: Jimy Zhang <jimy.zhang@umbratek.com> <jimy92@163.com>
# =============================================================================

import time
import sys
import argparse
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from utapi.utra.utra_report_status import UtraReportStatus100Hz
from utapi.utra.utra_report_status import UtraReportStatus10Hz
from utapi.utra.utra_report_config import UtraReportConfig10Hz

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = 'ubot report test'
    parser.add_argument("--m", help="[1: status10hz] [2: status100hz] [3: config]", default=1, type=int)
    parser.add_argument("--ip", help=" ", default="127.0.0.1", type=str)
    args = parser.parse_args()

    if args.m == 1:
        ubot = UtraReportStatus10Hz(args.ip)
    elif args.m == 2:
        ubot = UtraReportStatus100Hz(args.ip)
    elif args.m == 3:
        ubot = UtraReportConfig10Hz(args.ip)

    while 1:
        time.sleep(0.001)
        if ubot.is_update():
            ubot.print_data()
"""
python3 example/utra/demo01_report.py --ip 192.168.1.xxx --m 1
"""
