# aquarium_jetson_nano

Scratchpad repo for exchanging code and ideas during Jetson Orin Nano testing for Seattle Aquarium BlueROV project.

For further info, see the [docs/](docs/)

# Scripts:

## imx296_gst.sh

Streams one camera using gstreamer.   By default the gstreamer pipeline in the script publishes an RTSP stream -- it assumes an instance of [mediamtx](https://github.com/bluenviron/mediamtx) has been started on the Nano:

```
docker run --rm -it --network=host bluenviron/mediamtx:latest
```

The video can then be viewed using an RTSP client (`ffplay`, `VLC` etc)

See the comment in this script for saving the output to a file.

## imx296_stereo.sh

Streams _both_ cameras, compositing the two images side-by-side.   Publishes to a local RTSP server (see above).

## imx296_set_trigger.py

Configures camera trigger mode with `v4l2-ctl`.   For example, to set camera 0 to `EXTERNAL` mode:

```
./imx296_set_trigger.py -c 0 external
```

To set both cameras to "normal" triggering:

```
./imx296_set_trigger.py -c 0 -c 1  streaming
```

## imx296_trigger_gpios.py

Triggers both camera external trigger GPIOs at a fixed rate.   Only has an effect on cameras set the `EXTERNAL` mode.

## imx296_v4l.sh

Streams one camera using `v4l2-ctl`.   Note this doesn't produce any visible output, but does produce ">" hashes on each frame.   A good simple method for checking if the camera is running at all.

# Technical Details

# Trigger information

On the Orin NX devboard:

| Jetson Signal | Jetson Pin | GPIO Pin | VC Pin |
|---------------|------------|----------|--------|
| CAM0_PWDN | 114 | GPIO3_PH.06 | gpiochip0.49 | Trigger to sensor |
| CAM0_MCLK | 116 | |  | Flash from sensor |
| CAM1_PWDN | 120 | GPIO3_PAC.00 | gpiochip0.138 | Trigger to sensor |
| CAM1_MCLK | 122 | | | Flash from sensor |