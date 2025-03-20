#!/usr/bin/bash
#
# Uses the "glstereomix" GStreamer element to stream two nvargus cameras,
# combine them into a left-and-right composite image
# Set the type of output
# Default to screen (will fail if connected over SSH)
#
# Override on the command line with (for example):
#
#   OUTPUT=file ./imx296_gst.sh
#
# Valid values: file, rtsp or screen
OUTPUT=${OUTPUT:-screen}

. imx296_constants.sh

if [ $OUTPUT == "rtsp" ]; then
        GST_OUTPUT="x264enc speed-preset=veryfast tune=zerolatency ! h264parse ! rtspclientsink location=rtsp://localhost:8554/stereo"
elif [ $OUTPUT == "screen" ]; then
        GST_OUTPUT="nveglglessink"
elif [ $OUTPUT == "file" ]; then
        GST_OUTPUT="x264enc speed-preset=veryfast tune=zerolatency ! \
                h264parse ! mp4mux ! filesink location=test.mp4 -e"
elif [ $OUTPUT == "fake" ]; then
        GST_OUTPUT="fakesink"
fi


v4l2-ctl -d 0 -c bypass_mode=0 -c override_enable=1
v4l2-ctl -d 1 -c bypass_mode=0 -c override_enable=1
gst-launch-1.0 \
        nvcompositor name=comp ! 'video/x-raw(memory:NVMM)' ! nvvidconv ! 'video/x-raw' ! fakesink \
        nvarguscamerasrc sensor-id=0 $NVARGUS_CONFIG ! \
                'video/x-raw(memory:NVMM)',width=$IMG_WIDTH,height=$IMG_HEIGHT,'format=(string)NV12' ! \
                comp. \
        nvarguscamerasrc sensor-id=1 $NVARGUS_CONFIG ! \
                'video/x-raw(memory:NVMM)',width=$IMG_WIDTH,height=$IMG_HEIGHT,'format=(string)NV12' ! \
                comp.    
