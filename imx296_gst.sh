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
#   ffplay -rtsp_transport udp rtsp://<ip address of nano>:8554/mono
#
#
# Alternatively, To write an mp4 file, replace "rtspclientsink" at the end of the command with:
#
#   qtmux ! filesink location=test.mp4 
#
# (note the -e option is required to finalize the file)
#
# Note this requires "h264parse" which is in gstreamer1.0-plugins-bad
#           and "rtspclientsink" which is in gstreamer1.0-rtsp
#
# which might need to be installed:   sudo apt-get install -y gstreamer1.0-rtsp gstreamer1.0-plugins-bad
#

camera_num=${WHICH_CAMERA:-0}

. imx296_constants.sh

gst-launch-1.0 -ev nvarguscamerasrc sensor-id=$camera_num  ! \
            "video/x-raw(memory:NVMM),width=$IMG_WIDTH,height=$IMG_HEIGHT,framerate=$IMG_RATE/1" ! \
            nvvidconv ! 'video/x-raw' ! queue ! \
            x264enc speed-preset=veryfast tune=zerolatency ! \
            h264parse ! \
            rtspclientsink latency=200 location=rtsp://localhost:8554/mono

            # To save to a file, delete the "rtspclientsink" above, and use this instead
            #qtmux ! filesink location=test.mp4 -e
