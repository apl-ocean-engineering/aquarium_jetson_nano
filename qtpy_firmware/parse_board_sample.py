#!/usr/bin/env python3
#
# MWE for reading data from sensor board
#

import json
import serial


SERIAL_PORT="/dev/ttyQtPy"

if __name__=="__main__":

    with serial.Serial(SERIAL_PORT, 19200, timeout=1.5) as ser:
        while True:
            ser_in = ser.readline()
            print(ser_in)

            try:
                results = json.loads(ser_in)

                print(f"Parsed results: {results}")
            except json.decoder.JSONDecodeError:
                pass
