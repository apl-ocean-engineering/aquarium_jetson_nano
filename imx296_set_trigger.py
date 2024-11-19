#!/usr/bin/env python3
#
# From the VC Github page (https://github.com/VC-MIPI-modules/vc_mipi_nvidia/blob/master/doc/TRIGGER_MODE.md)
#
# Activate a trigger mode by
#
# v4l2-ctl -c trigger_mode=<trigger mode number>
#
# The trigger mode remains set until it is deactivated with
#
# v4l2-ctl -c trigger_mode=0
#
# IMX392 supports:
#   1. external
#   2. pulsewidth
#   3. self
#   4. single:  v4l2-ctl -c single_trigger=1

import subprocess
import argparse
from enum import Enum

class TriggerMode(Enum):
    INTERNAL = 0
    EXTERNAL = 1
    PULSEWIDTH = 2
    SELF = 3
    SINGLE = 4

if __name__=="__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("mode", choices=['internal', 'external', 'pulsewidth', 'self', 'single'])
    parser.add_argument("--camera", "-c", nargs="*", default=[], help="Camera(s) to modify (0,1)")

    args = parser.parse_args()

    mode = TriggerMode[ args.mode.upper() ]

    if len(args.camera) == 0:
        parser.error("No cameras specified, not doing anything")

    for cam in args.camera:
        print(f"Configuring camera {cam}")
        subprocess.run(["sudo", "v4l2-ctl", "-d", cam, "-c", f"trigger_mode={mode.value}"])