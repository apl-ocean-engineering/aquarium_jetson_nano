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

```
ACCELEROMETER:                                                                                                                                                                                                                                           
X Velocity Random Walk:  0.00101 m/s/sqrt(s)  0.06064 m/s/sqrt(hr)                                                                                                                                                                                       
Y Velocity Random Walk:  0.00099 m/s/sqrt(s)  0.05930 m/s/sqrt(hr)                                                                                                                                                                                       
Z Velocity Random Walk:  0.00135 m/s/sqrt(s)  0.08091 m/s/sqrt(hr)                                                                                                                                                                                       
X Bias Instability:  0.00012 m/s^2  1584.33538 m/hr^2                                                                                                                                                                                                    
Y Bias Instability:  0.00014 m/s^2  1805.84251 m/hr^2                                                                                                                                                                                                    
Z Bias Instability:  0.00020 m/s^2  2624.17320 m/hr^2
X Accel Random Walk:  0.00002 m/s^2/sqrt(s)
Y Accel Random Walk:  0.00002 m/s^2/sqrt(s)
Z Accel Random Walk:  0.00005 m/s^2/sqrt(s)
GYROSCOPE:
X Angle Random Walk:  0.00293 deg/sqrt(s)  0.17602 deg/sqrt(hr)
Y Angle Random Walk:  0.00299 deg/sqrt(s)  0.17926 deg/sqrt(hr)
Z Angle Random Walk:  0.00303 deg/sqrt(s)  0.18195 deg/sqrt(hr)
X Bias Instability:  0.00023 deg/s  0.82319 deg/hr
Y Bias Instability:  0.00026 deg/s  0.95120 deg/hr
Z Bias Instability:  0.00020 deg/s  0.73373 deg/hr
X Rate Random Walk:  0.00004 deg/s/sqrt(s)
Y Rate Random Walk:  0.00004 deg/s/sqrt(s)
Z Rate Random Walk:  0.00004 deg/s/sqrt(s)
```

![](2025-06-11-IMU-Calibration/acceleration.png)

![](2025-06-11-IMU-Calibration/gyro.png)

and an `imu.yaml`:

```
#Accelerometer
accelerometer_noise_density: 0.0013485615577481405 
accelerometer_random_walk: 4.8764403232898057e-05 

#Gyroscope
gyroscope_noise_density: 5.292821371595905e-05 
gyroscope_random_walk: 7.067414132646592e-07 

rostopic: '/imu' 
update_rate: 200 
```

# Camera calibration

For fun, try the camera calibration (in air, since we don't have an in-air calibration)

Took data with camera imagery of Kalibr board.

Install Kalibr per [their instructions.](https://github.com/ethz-asl/kalibr/wiki/installation)

```
kalibr_calibrate_cameras --bag [filename.bag] --topics [TOPIC_0 ... TOPIC_N] --models [MODEL_0 ... MODEL_N] --target aprilgrid.yaml
```

# Camera-IMU Calibration

Then:

```
kalibr_calibrate_imu_camera --bag [filename.bag] --cam [camchain.yaml] --imu imu.yaml --target aprilgrid.yaml
```