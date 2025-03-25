#!/usr/bin/bash
#
# Streams one cameras using Gstreamer.
#
# Set the type of output
# Default to screen (will fail if connected over SSH)
#
# Override on the command line with (for example):
#
#   OUTPUT=file ./imx296_gst.sh
#
# Valid values: file, rtsp or screen
OUTPUT=${OUTPUT:-screen}

camera_num=${WHICH_CAMERA:-0}
. imx296_constants.sh

if [ $OUTPUT == "rtsp" ]; then
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
        GST_OUTPUT="x264enc speed-preset=veryfast tune=zerolatency ! h264parse ! rtspclientsink location=rtsp://localhost:8554/mono"
elif [ $OUTPUT == "screen" ]; then
        # Output to the screen
        GST_OUTPUT="nveglglessink"
elif [ $OUTPUT == "file" ]; then
        # Save to a file
        GST_OUTPUT="x264enc speed-preset=veryfast tune=zerolatency ! \
                h264parse ! mp4mux ! filesink location=test.mp4 -e"
elif [ $OUTPUT == "fake" ]; then
        GST_OUTPUT="fpsdisplaysink video-sink=fakesink"
fi

echo "Launching camera $camera_num"

#configure_cameras $camera_num
gst-launch-1.0 -ev nvarguscamerasrc sensor-id=$camera_num $NVARGUS_CONFIG ! \
            "video/x-raw(memory:NVMM),width=$IMG_WIDTH,height=$IMG_HEIGHT",framerate=10/1 ! \
            nvvidconv ! 'video/x-raw' ! queue ! $GST_OUTPUT
