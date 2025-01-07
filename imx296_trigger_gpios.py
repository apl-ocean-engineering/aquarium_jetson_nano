#!/usr/bin/env python3
#
# Sample program which sends external triggers to VC cameras
#
# Only effective if the cameras are set to EXTERNAL mode 
# (this program does not configure the cameras automatically)

import gpiod
import argparse
import time

from gpiod.line import Direction, Value

def toggle_value(value):
    if value == Value.INACTIVE:
        return Value.ACTIVE
    return Value.INACTIVE

def toggle_multiple_line_values(chip_path, line_values):
    value_str = {Value.ACTIVE: "Active", Value.INACTIVE: "Inactive"}

    request = gpiod.request_lines(
        chip_path,
        consumer="imx296_external_trigger",
        config={
            tuple(line_values.keys()): gpiod.LineSettings(direction=Direction.OUTPUT)
        },
        output_values=line_values,
    )

    while True:
        print(
            " ".join("{}={}".format(l, value_str[v]) for (l, v) in line_values.items())
        )
        time.sleep(0.1)
        for l, v in line_values.items():
            line_values[l] = toggle_value(v)
        request.set_values(line_values)


CAM0_TRIGGER = 49
CAM1_TRIGGER = 138

if __name__ == "__main__":
    try:
        toggle_multiple_line_values(
            "/dev/gpiochip0", {CAM0_TRIGGER: Value.ACTIVE, CAM1_TRIGGER: Value.ACTIVE}
        )
    except OSError as ex:
        print(ex, "\nCustomise the example configuration to suit your situation")