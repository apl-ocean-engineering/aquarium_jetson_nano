Just check, I installed a GS camera onto a Raspi4, and a Raspi High Quality (HQ) camera onto the CAM1 port of the Nano (with a GS still on  CAM0)

# GS on Raspi

Raspi is running "Bookworm".  Detected camera automatically on bootup:

```shell
[    7.633859] imx296 10-001a: found IMX296LQ (17.0C)
```

```shell
pi@bookworm4:~ $ v4l2-ctl --all -d 0
Driver Info:
	Driver name      : unicam
	Card type        : unicam
	Bus info         : platform:fe801000.csi
	Driver version   : 6.6.31
	Capabilities     : 0xa5a00001
		Video Capture
		Metadata Capture
		Read/Write
		Streaming
		Extended Pix Format
		Device Capabilities
	Device Caps      : 0x25200001
		Video Capture
		Read/Write
		Streaming
		Extended Pix Format
Media Driver Info:
	Driver name      : unicam
	Model            : unicam
	Serial           :
	Bus info         : platform:fe801000.csi
	Media version    : 6.6.31
	Hardware revision: 0x00000000 (0)
	Driver version   : 6.6.31
Interface Info:
	ID               : 0x03000005
	Type             : V4L Video
Entity Info:
	ID               : 0x00000003 (3)
	Name             : unicam-image
	Function         : V4L2 I/O
	Flags            : default
	Pad 0x01000004   : 0: Sink
	  Link 0x02000007: from remote pad 0x1000002 of entity 'imx296 10-001a' (Camera Sensor): Data, Enabled, Immutable
Priority: 2
Video input : 0 (unicam-image: ok)
Format Video Capture:
	Width/Height      : 640/480
	Pixel Format      : 'YUYV' (YUYV 4:2:2)
	Field             : None
	Bytes per Line    : 1280
	Size Image        : 614400
	Colorspace        : sRGB
	Transfer Function : sRGB
	YCbCr/HSV Encoding: ITU-R 601
	Quantization      : Limited Range
	Flags             :
```

Running:

```
pi@bookworm4:~ $ rpicam-still -o test.jpg -t 1
[0:59:50.354145420] [1231]  INFO Camera camera_manager.cpp:313 libcamera v0.3.0+65-6ddd79b5
[0:59:50.397587914] [1234]  WARN RPiSdn sdn.cpp:40 Using legacy SDN tuning - please consider moving SDN inside rpi.denoise
[0:59:50.400438282] [1234]  INFO RPI vc4.cpp:446 Registered camera /base/soc/i2c0mux/i2c@1/imx296@1a to Unicam device /dev/media2 and ISP device /dev/media0
[0:59:50.400573133] [1234]  INFO RPI pipeline_base.cpp:1104 Using configuration file '/usr/share/libcamera/pipeline/rpi/vc4/rpi_apps.yaml'
Preview window unavailable
Mode selection for 728:544:12:P
    SRGGB10_CSI2P,1456x1088/0 - Score: 1318
[0:59:50.402557951] [1231]  INFO Camera camera.cpp:1183 configuring streams: (0) 728x544-YUV420 (1) 1456x1088-SBGGR10_CSI2P
[0:59:50.403061374] [1234]  INFO RPI vc4.cpp:621 Sensor: /base/soc/i2c0mux/i2c@1/imx296@1a - Selected sensor format: 1456x1088-SBGGR10_1X10 - Selected unicam format: 1456x1088-pBAA
Mode selection for 1456:1088:12:P
    SRGGB10_CSI2P,1456x1088/0 - Score: 1000
[0:59:51.281123101] [1231]  INFO Camera camera.cpp:1183 configuring streams: (0) 1456x1088-YUV420 (1) 1456x1088-SBGGR10_CSI2P
[0:59:51.282881013] [1234]  INFO RPI vc4.cpp:621 Sensor: /base/soc/i2c0mux/i2c@1/imx296@1a - Selected sensor format: 1456x1088-SBGGR10_1X10 - Selected unicam format: 1456x1088-pBAA
Still capture image received
```

![test](https://github.com/user-attachments/assets/4ca47888-6ea4-46e1-9a45-d43b2f230a31)

Uh... obviously not focused.


# IMX477 on Jetson Nano

Use `jetson-io.py` to install `tegra234-p3767-camera-p3768-imx477-dual.dtbo`

Hm, interesting:

```shell
[   11.015472] imx477 9-001a: sensor_common_parse_image_props:active_l property missing
[   11.015476] imx477 9-001a: Failed to read mode0 image props
[   11.015479] imx477 9-001a: Could not initialize sensor properties.
[   11.015481] imx477 9-001a: Failed to initialize imx477
[   11.015483] imx477 9-001a: tegra camera driver registration failed
[   11.015523] imx477: probe of 9-001a failed with error -61
[   11.017276] imx477 10-001a: sensor_common_parse_image_props:active_l property missing
[   11.017281] imx477 10-001a: Failed to read mode0 image props
[   11.017285] imx477 10-001a: Could not initialize sensor properties.
[   11.017287] imx477 10-001a: Failed to initialize imx477
[   11.017289] imx477 10-001a: tegra camera driver registration failed
```

Switch to a unit which has [R8 removed](https://developer.ridgerun.com/wiki/index.php/Raspberry_Pi_HQ_camera_IMX477_Linux_driver_for_Jetson#Compatibility_with_NVIDIA®Jetson™_Platforms):

Hm, no change.

Just for laughs, move IMX477 to CAM0 and install IMX219 in CAM1.  Use "Camera IMX219-A and IMX477-C" (`tegra234-p3767-camera-p3768-imx219-imx477.dtbo`)

Well, that didn't work:

```shell
[   10.652709] imx219 10-0010: sensor_common_parse_image_props:active_l property missing
[   10.652718] imx219 10-0010: Failed to read mode0 image props
[   10.652723] imx219 10-0010: Could not initialize sensor properties.
[   10.652725] imx219 10-0010: Failed to initialize imx219
[   10.652728] imx219 10-0010: tegra camera driver registration failed
[   10.652768] imx219: probe of 10-0010 failed with error -61
[   10.656655] imx477 9-001a: sensor_common_parse_image_props:active_l property missing
[   10.656661] imx477 9-001a: Failed to read mode0 image props
[   10.656665] imx477 9-001a: Could not initialize sensor properties.
[   10.656668] imx477 9-001a: Failed to initialize imx477
[   10.656671] imx477 9-001a: tegra camera driver registration failed
[   10.656711] imx477: probe of 9-001a failed with error -61
```

Try "Camera IMX477-A and IMX219-C" (`tegra234-p3767-camera-p3768-imx477-imx219.dtbo`)

Do clean install of Jetpack 6.1

After reinstalling Jetpack, it did find IMX219 (dual IMX219 is in the default dtb).   Try "Camera IMX477-A and IMX219-C" again.

Finds both cameras!
