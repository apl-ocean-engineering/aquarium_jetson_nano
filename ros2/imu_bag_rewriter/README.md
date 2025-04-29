Very simple node to rewrite ROS2 bagfiles containing an `Imu` topic with incorrect header timestamps.

Uses the _bag_ timestamps, and assumes time difference between IMU readings is constant.

To use:

```
pip install -e .
imu_bag_rewrite <ros2 bag directory>
```

It will automatically create the output in the current directory, or specify an output location with `-o <output_bag>`
