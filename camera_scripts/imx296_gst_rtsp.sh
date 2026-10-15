#!/usr/bin/bash
#
# Streams one cameras using Gstreamer.


camera_num=${WHICH_CAMERA:-1}
. imx296_constants.sh

GST_OUTPUT="x264enc speed-preset=veryfast tune=zerolatency ! h264parse ! rtspclientsink location=rtsp://localhost:8554/left"

echo "Launching camera $camera_num"

configure_cameras $camera_num
gst-launch-1.0 -e nvarguscamerasrc sensor-id=$camera_num $NVARGUS_CONFIG ! \
            "video/x-raw(memory:NVMM),width=$IMG_WIDTH,height=$IMG_HEIGHT",framerate=10/1 ! \
            nvvidconv ! 'video/x-raw' ! queue ! $GST_OUTPUT
