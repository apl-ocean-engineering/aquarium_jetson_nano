Firmware for the QtPy "sensor module."  The standard Nano installed will create symlinks such that:

* A symlink will be created at `/dev/qtpy` for the USB drive function
* A symlink will be created at `/dev/ttyQtPy` for the serial function

The current boards have CircuitPython 9.2.4 installed.

To install this firmware:

- Download and uncompress the [CircuitPython library](https://circuitpython.org/libraries) for the correct version of circuit python.
- Install the following libraries from the library bundle to `/mnt/qtpy/lib`:
    - *adafruit_bme280*
    - *adafruit_bus_device*

- Copy *code.py* from this directory to `/mnt/qtpy`

The python script `parse_board_sample.py` can be used to check if the output is valid JSON:

```sh
python3 parse_board_sample.py
```
