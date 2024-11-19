#!/usr/bin/env python3
#
# Set the trigger mode on one or more cameras
#
#
# From the VC Github page 
# (https://github.com/VC-MIPI-modules/vc_mipi_nvidia/blob/master/doc/TRIGGER_MODE.md)
#
# The command line is:
#
#   v4l2-ctl -c trigger_mode=<trigger mode number>
#
# The trigger mode remains set until it is deactivated with
#
#   v4l2-ctl -c trigger_mode=0
#
# IMX392 supports:
#   0. trigger disabled (streaming)
#   1. external
#   2. pulsewidth
#   3. self
#   4. single:  v4l2-ctl -c single_trigger=1

import subprocess
import argparse
from enum import Enum

class TriggerMode(Enum):
    STREAMING = 0
    EXTERNAL = 1
    PULSEWIDTH = 2
    SELF = 3
    SINGLE = 4

if __name__=="__main__":

    parser = argparse.ArgumentParser()

    mode_choices = [t.name.lower() for t in TriggerMode]
    parser.add_argument("mode", 
                        choices=mode_choices,
                        help=f"Trigger mode (options: {','.join(mode_choices)})")
    parser.add_argument("--camera", "-c", action="append",
                        default=[], help="Camera(s) to modify (0,1).  Can be specified multiple times.")

    args = parser.parse_args()

    mode = TriggerMode[ args.mode.upper() ]

    if len(args.camera) == 0:
        parser.error("No cameras specified, not doing anything")

    for cam in args.camera:
        print(f"Configuring camera {cam} to {mode.name}")
        subprocess.run(["sudo", "v4l2-ctl", "-d", cam, "-c", f"trigger_mode={mode.value}"])