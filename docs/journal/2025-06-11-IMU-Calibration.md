Notes while working on camera-IMU calibration.

Preliminary plan is to use [Kalibr](https://github.com/ethz-asl/kalibr/wiki/camera-imu-calibration);  noting this will require recording data in ROS2 bags and converting to ROS1 for processing.

# IMU Characterization

Per their instructions, start by characterizing the IMU using [ori-drs/allan_variance_ros](https://github.com/ori-drs/allan_variance_ros).

1. Record 4 hours of IMU data:

```
ros2 launch vectornav vectornav.launch.py
```

```
timeout 14400 ros2 bag record -s mcap --storage-preset-profile zstd_fast /imu
```

2. Convert ROS2 bag to ROS1

```
rosbags-convert --src rosbag2_imu_characterization --dst rosbag1_imu_characterization --compress lz4
```

3. Build [allan_variance_ros](https://github.com/ori-drs/allan_variance_ros) in a ROS1 environment (I used a rosvenv).

4. Per the README, reorganize ROS messages by timestamp:

Note the allan_variance executable looks for a _directory_ and loads all of the bagfiles in it.   Put the cooked bag into a directory:


```
mkdir cooked_data
rosrun allan_variance_ros cookbag.py --input rosbag1_imu_characterization.bag --output cooked_data/cooked_imu_characterization.bag
```

4. Create a configuration file `odometry_imu.yaml`:

```
imu_topic: "/imu"
imu_rate: 200
measure_rate: 200 # Rate to which imu data is subsampled
sequence_time: 10800 # 3 hours in seconds
```

5. Run the Allan Variance computation tool (example config files provided):

(Note this is a rosrun, you need to manually launch) a roscore...

```
rosrun allan_variance_ros allan_variance cooked_data odometry_imu.yaml
```

This will create a file `allan_variance.csv` in `cooked_data/`

6.  The next step is to visualize the plots and get parameters. For this run:

```
rosrun allan_variance_ros analysis.py --data cooked_data/allan_variance.csv --config odometry_imu.yaml
```

This will produce some text output and graphs.
