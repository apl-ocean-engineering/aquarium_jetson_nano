Vision Components IMX296 module arrived today from Mouser.

After adjusting the OVERLAY, got this:

```shell
[   13.398382] vc_mipi 9-001a: vc_mod_setup(): Unable to get module I2C client for address 0x10
[   13.398392] vc_mipi 9-001a: vc_probe(): Error in vc_core_init!
[   13.398705] vc_mipi 10-001a: vc_probe(): Probing UNIVERSAL VC MIPI Driver (v0.18.1)
[   13.555283] using random self ethernet address
[   13.555292] using random host ethernet address
[   13.578816] i2c 10-0010: +--- VC MIPI Camera -----------------------------------+
[   13.578827] i2c 10-0010: | MANUF. | Vision Components               MID: 0x0427 |
[   13.578831] i2c 10-0010: | MODULE | ID:  0x0296                     REV:   0043 |
[   13.578834] i2c 10-0010: | SENSOR | SONY IMX296C                                |
[   13.578838] i2c 10-0010: +--------+---------------------------------------------+
[   13.578840] i2c 10-0010: +--- Sensor Registers ------+--------+--------+--------+
[   13.578842] i2c 10-0010: |                           | low    | mid    | high   |
[   13.578844] i2c 10-0010: +---------------------------+--------+--------+--------+
[   13.578846] i2c 10-0010: | idle                      | 0x3000 |        |        |
[   13.578849] i2c 10-0010: | horizontal start          | 0x3310 | 0x3311 |        |
[   13.578852] i2c 10-0010: | vertical start            | 0x3312 | 0x3313 |        |
[   13.578855] i2c 10-0010: | horizontal end            | 0x0000 | 0x0000 |        |
[   13.578857] i2c 10-0010: | vertical end              | 0x4182 | 0x4183 |        |
[   13.578859] i2c 10-0010: | hor. output width         | 0x3314 | 0x3315 |        |
[   13.578860] i2c 10-0010: | ver. output height        | 0x3316 | 0x3317 |        |
[   13.578861] i2c 10-0010: | exposure                  | 0x308d | 0x308e | 0x308f |
[   13.578863] i2c 10-0010: | gain                      | 0x3204 | 0x3205 |        |
[   13.578864] i2c 10-0010: +---------------------------+--------+--------+--------+
[   13.578865] i2c 10-0010: | clock for ext. trigger    | 54000000 Hz              |
[   13.578866] i2c 10-0010: | pixel clock               | 74250000 Hz              |
[   13.578868] i2c 10-0010: | shutter offset            |      770 us              |
[   13.578869] i2c 10-0010: +---------------------------+--------------------------+
[   13.578870] i2c 10-0010: +--- Module Modes -------+---------+---------+---------+
[   13.578870] i2c 10-0010: |  # | rate    | lanes   | format  | type    | binning |
[   13.578871] i2c 10-0010: +----+---------+---------+---------+---------+---------+
[   13.578873] i2c 10-0010: |  0 |    1188 |       1 | RAW10   | STREAM  |       0 |
[   13.578876] i2c 10-0010: |  1 |    1188 |       1 | RAW10   | EXT.TRG |       0 |
[   13.578878] i2c 10-0010: +----+---------+---------+---------+---------+---------+
[   13.578880] i2c 10-0010: vc_init_ctrl_imx296(): Initialising module control for IMX296
[   13.578886] i2c 10-0010: +-------+--------+------------+-----------+
[   13.578887] i2c 10-0010: | lanes | format | exposure   | framerate |
[   13.578888] i2c 10-0010: |       |        | max [us]   | max [mHz] |
[   13.578889] i2c 10-0010: +-------+--------+------------+-----------+
[   13.578890] i2c 10-0010: |     1 | RAW10  |   15533515 |     60816 |
[   13.578892] i2c 10-0010: +-------+--------+------------+-----------+
[   13.578893] i2c 10-0010: VC MIPI Core successfully initialized
[   13.578896] vc_mipi 10-001a: vc_init_io(): Init trigger and flash mode
[   13.578902] i2c 10-0010: vc_mod_set_trigger_mode(): Set trigger mode: DISABLED
[   13.578905] i2c 10-0010: vc_mod_set_io_mode(): Set IO mode: DISABLED
[   13.578909] vc_mipi 10-001a: vc_init_frmfmt(): Init frame (width: 1440, height: 1080, fps: 0)
[   13.578912] vc_mipi 10-001a: vc_init_binning(): Init binning modes
[   13.579172] vc_mipi 10-001a: tegracam sensor driver:vc_mipi_v2.0.6
[   13.579250] tegra-camrtc-capture-vi tegra-capture-vi: subdev vc_mipi 10-001a bound
[   13.611503] loop0: detected capacity change from 0 to 32768
[   13.639487] vc_mipi 10-001a: vc_core_set_num_lanes(): Set number of lanes 1
[   13.639500] vc_mipi 10-001a: vc_init_lanes(): Init lanes (num_lanes: 1)
[   13.639503] vc_mipi 10-001a: vc_init_tegra_controls(): Read control gain (min: 0, max: 48000, default: 0)
[   13.639506] vc_mipi 10-001a: vc_init_tegra_controls(): Overwrite control exposure (min: 1, max: 15533515, default: 10000)
[   13.639508] vc_mipi 10-001a: vc_init_tegra_controls(): Overwrite control framerate (min: 0, max: 60816, default: 0)
```

And

```shell
$ v4l2-ctl --all -d 0

Driver Info:
        Driver name      : tegra-video
        Card type        : vi-output, vc_mipi 10-001a
        Bus info         : platform:tegra-capture-vi:1
        Driver version   : 5.15.148
        Capabilities     : 0x84200001
                Video Capture
                Streaming
                Extended Pix Format
                Device Capabilities
        Device Caps      : 0x04200001
                Video Capture
                Streaming
                Extended Pix Format
Media Driver Info:
        Driver name      : tegra-camrtc-ca
        Model            : NVIDIA Tegra Video Input Device
        Serial           :
        Bus info         :
        Media version    : 5.15.148
        Hardware revision: 0x00000003 (3)
        Driver version   : 5.15.148
Interface Info:
        ID               : 0x0300000b
        Type             : V4L Video
Entity Info:
        ID               : 0x00000009 (9)
        Name             : vi-output, vc_mipi 10-001a
        Function         : V4L2 I/O
        Pad 0x0100000a   : 0: Sink
          Link 0x0200000f: from remote pad 0x1000003 of entity '13e00000.host1x:nvcsi@15a00000-' (Unknown sub-device (0002000a)): Data, Enabled
Priority: 2
Video input : 0 (Camera 1: no power)
Format Video Capture:
        Width/Height      : 1440/1080
        Pixel Format      : 'RG10' (10-bit Bayer RGRG/GBGB)
        Field             : None
        Bytes per Line    : 2880
        Size Image        : 3110400
        Colorspace        : sRGB
        Transfer Function : Default (maps to sRGB)
        YCbCr/HSV Encoding: Default (maps to ITU-R 601)
        Quantization      : Default (maps to Full Range)
        Flags             :
Selection Video Capture: crop, Left 0, Top 0, Width 0, Height 0, Flags:
Selection Video Output: crop, Left 0, Top 0, Width 0, Height 0, Flags:

Camera Controls

                     group_hold 0x009a2003 (bool)   : default=0 value=0 flags=execute-on-write
                    sensor_mode 0x009a2008 (int64)  : min=0 max=1 step=1 default=0 value=0 flags=slider
                           gain 0x009a2009 (int64)  : min=0 max=48001 step=100 default=0 value=0 flags=slider
                       exposure 0x009a200a (int64)  : min=1 max=1000001 step=1 default=10000 value=1 flags=slider
                     frame_rate 0x009a200b (int64)  : min=100 max=60000 step=100 default=60000 value=100 flags=slider
                   trigger_mode 0x009a200f (int)    : min=0 max=7 step=1 default=0 value=0
                        io_mode 0x009a2010 (int)    : min=0 max=5 step=1 default=0 value=0
                    black_level 0x009a2011 (int)    : min=0 max=100000 step=1 default=0 value=0
                 single_trigger 0x009a2012 (button) : value=0 flags=write-only, execute-on-write
                   binning_mode 0x009a2013 (int)    : min=0 max=7 step=1 default=0 value=0
           sensor_configuration 0x009a2032 (u32)    : min=0 max=4294967295 step=1 default=0 dims=[22] flags=read-only, volatile, has-payload
         sensor_mode_i2c_packet 0x009a2033 (u32)    : min=0 max=4294967295 step=1 default=0 dims=[1026] flags=read-only, volatile, has-payload
      sensor_control_i2c_packet 0x009a2034 (u32)    : min=0 max=4294967295 step=1 default=0 dims=[1026] flags=read-only, volatile, has-payload
                    bypass_mode 0x009a2064 (intmenu): min=0 max=1 default=0 value=0 (0 0x0)
                                0: 0 (0x0)
                                1: 1 (0x1)
                override_enable 0x009a2065 (intmenu): min=0 max=1 default=0 value=0 (0 0x0)
                                0: 0 (0x0)
                                1: 1 (0x1)
                   height_align 0x009a2066 (int)    : min=1 max=16 step=1 default=1 value=1
                     size_align 0x009a2067 (intmenu): min=0 max=2 default=0 value=0 (1 0x1)
                                0: 1 (0x1)
                                1: 65536 (0x10000)
                                2: 131072 (0x20000)
               write_isp_format 0x009a2068 (int)    : min=1 max=1 step=1 default=1 value=1
       sensor_signal_properties 0x009a2069 (u32)    : min=0 max=4294967295 step=1 default=0 dims=[30][18] flags=read-only, has-payload
        sensor_image_properties 0x009a206a (u32)    : min=0 max=4294967295 step=1 default=0 dims=[30][18] flags=read-only, has-payload
      sensor_control_properties 0x009a206b (u32)    : min=0 max=4294967295 step=1 default=0 dims=[30][36] flags=read-only, has-payload
              sensor_dv_timings 0x009a206c (u32)    : min=0 max=4294967295 step=1 default=0 dims=[30][16] flags=read-only, has-payload
               low_latency_mode 0x009a206d (bool)   : default=0 value=0
               preferred_stride 0x009a206e (int)    : min=0 max=65535 step=1 default=0 value=0
    override_capture_timeout_ms 0x009a206f (int)    : min=-1 max=2147483647 step=1 default=5000 value=5000
```

```shell
$ v4l2-ctl --device /dev/video0 --list-formats-ext
ioctl: VIDIOC_ENUM_FMT
        Type: Video Capture

        [0]: 'RG10' (10-bit Bayer RGRG/GBGB)
                Size: Discrete 1440x1080
                        Interval: Discrete infs (0.000 fps)
```

I'm able to get frames through V4L2:

```shell
v4l2-ctl -d 0 --stream-mmap --stream-count 10
```

After some adjustments to device tree ( [vc-jetson-driver-release](https://github.com/apl-ocean-engineering/vc-jetson-driver-release) [commit 999ea01](https://github.com/apl-ocean-engineering/vc-jetson-driver-release/commit/a92b25748f1028597dfc9b8cffb4fbcddc6df82f)), I get gstreamer to work.  Here's a sample:

```
gst-launch-1.0 nvarguscamerasrc sensor-id=0  ! "video/x-raw(memory:NVMM),width=1440,height=1080,framerate=10/1" ! nvvidconv ! x264enc ! h264parse ! rtspclientsink location=rtsp://localhost:8554/test
```

Here's a test scripts:


```
#!/usr/bin/sh
#
# Assumes a mediamtx instance is running on localhost:
#
#   docker run --rm -it --network=host bluenviron/mediamtx:latest
#
# Can be played on the desktop with:
#
#   ffplay -rtsp_transport udp rtsp://<ip address of nano>:8554/test

gst-launch-1.0 nvarguscamerasrc sensor-id=0  ! "video/x-raw(memory:NVMM),width=1440,height=1080,framerate=30/1" ! \
            nvvidconv ! 'video/x-raw' ! queue ! \
            x264enc speed-preset=veryfast tune=zerolatency ! \
            h264parse ! \
            rtspclientsink location=rtsp://localhost:8554/test
```

