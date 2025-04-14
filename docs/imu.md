The Nano system contains a VectorNav [VN100 Rugged](https://www.vectornav.com/products/detail/vn-100?gad_source=1&gbraid=0AAAAAD2EOMMHBF22FjTunN2XF20KxFCOX&gclid=CjwKCAjw5PK_BhBBEiwAL7GTPQHpKoln6EM5mMhLmxXkyfay3LzAJRN4Dq_Y6IyOus5SB7GWh_xfoRoCsJkQAvD_BwE) IMU.   It connects to the Nano via USB and appears as the serial device `/dev/ttyUSB0`, but I've installed a udev rule to create a symlink to `/dev/ttyVectornav`

In most cases, I configure the device for 921600 baud.  The sensor output is binary, but can be observed with:

```
picocom -b 921600 /dev/ttyVectornav
```

I have briefly tried the following software:

* For ROS1, [ntnu-arl/vectornav](//github.com/ntnu-arl/vectornav.git)
* For ROS2, [martindeegan/vectornav_ros2](//github.com/martindeegan/vectornav_ros2.git)

I also tried the `ros2` branch of [dawonn/vectornav](https://github.com/dawonn/vectornav/tree/ros2) but could not get it to reliably communicate with the IMU.

## Documentation

* [VN100 Developer's Manual](resources/Vector_NAV_VN100_Rugged_Developers_Manual.pdf)