#!/usr/bin/bash
#
# Streams one cameras using Gstreamer.
# The default configuration generates an RTSP stream.
# This asumes a mediamtx instance is already running on the nano:
#
#   docker run --rm -it --network=host bluenviron/mediamtx:latest
#
# The stream can then be played with an RTSP client on a desktop, for example:
#
#   ffplay -rtsp_transport udp rtsp://<ip address of nano>:8554/stereo
#
#
# Alternatively, To write an mp4 file, replace "rtspclientsink" with:
#
#   qtmux ! filesink location=test.mp4 
#
# (note the -e option is required to finalize the file)

WHICH_CAMERA=0

. imx296_constants.sh

gst-launch-1.0 -ev nvarguscamerasrc sensor-id=$WHICH_CAMERA  ! \
            "video/x-raw(memory:NVMM),width=$IMG_WIDTH,height=$IMG_HEIGHT,framerate=$IMG_RATE/1" ! \
            nvvidconv ! 'video/x-raw' ! queue ! \
            x264enc speed-preset=veryfast tune=zerolatency ! \
            h264parse ! \
            rtspclientsink location=rtsp://localhost:8554/test

            #qtmux ! filesink location=test.mp4 -e
