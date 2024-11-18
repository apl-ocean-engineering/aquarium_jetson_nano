#!/usr/bin/sh
#
# This asumes a mediamtx instance is already running on the nano:
#
#   docker run --rm -it --network=host bluenviron/mediamtx:latest
#
# It can then be played on a desktop with:
#
#   ffplay -rtsp_transport udp rtsp://<ip address of nano>:8554/stereo

gst-launch-1.0 nvarguscamerasrc sensor-id=0  ! "video/x-raw(memory:NVMM),width=1440,height=1080,framerate=30/1" ! \
            nvvidconv ! 'video/x-raw' ! queue ! \
            x264enc speed-preset=veryfast tune=zerolatency ! \
            h264parse ! \
            rtspclientsink location=rtsp://localhost:8554/test