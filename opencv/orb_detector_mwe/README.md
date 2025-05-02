A python script for testing the ORB detector.   This script reads images from ROS bags;  it uses [rosbags](https://gitlab.com/ternaris/rosbags) and does not require that ROS1 / ROS2.

To use:

```shell
pip install -e .
orb_detect --count 10 <path to bagfile(s)>
```

It will produce output in the directory `output/`

See `orb_detect --help` for options.