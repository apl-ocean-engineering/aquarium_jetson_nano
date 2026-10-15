#!/usr/bin/bash
#
# Streams one IMX900 cameras using Gstreamer.

camera_num=${WHICH_CAMERA:-0}
. imx900_constants.sh


# This asumes a mediamtx instance is already running on the nano:
#
#   docker run --rm -it --network=host bluenviron/mediamtx:latest
#
# The stream can then be played with an RTSP client on a desktop, for example:
#
#   ffplay -rtsp_transport udp rtsp://<ip address of nano>:8554/mono
#
# Note this requires "h264parse" which is in gstreamer1.0-plugins-bad
#           and "rtspclientsink" which is in gstreamer1.0-rtsp
#
# which might need to be installed:   sudo apt-get install -y gstreamer1.0-rtsp gstreamer1.0-plugins-bad
#
GST_OUTPUT="x264enc speed-preset=veryfast tune=zerolatency ! h264parse ! rtspclientsink location=rtsp://localhost:8554/right"

echo "Launching camera $camera_num"

configure_cameras $camera_num
gst-launch-1.0 -e nvarguscamerasrc sensor-id=$camera_num $NVARGUS_CONFIG ! \
            "video/x-raw(memory:NVMM),width=$IMG_WIDTH,height=$IMG_HEIGHT",framerate=30/1 ! \
            nvvidconv ! 'video/x-raw' ! queue ! $GST_OUTPUT

#gst-launch-1.0 v4l2src device=/dev/video0 ! "video/x-raw,format=GRAY8,width=$IMG_WIDTH,height=$IMG_HEIGHT",framerate=30/1 ! fakesink 
#videoconvert ! queue ! $GST_OUTPUT