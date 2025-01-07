#!/usr/bin/bash
#
# Stream 100 frames from from one camera using v4l2
#
# Note this doesn't actually stream the video anywhere useful
# but you do get to see tickmarks as frames come in
#
# Defaults for camera 0 (left?), to set right:
#
#  WHICH_CAMERA=1  ./imx296_v4l.sh 

camera_num=${WHICH_CAMERA:-0}

. imx296_constants.sh

 v4l2-ctl --set-fmt-video=width=$IMG_WIDTH,height=$IMG_HEIGHT,pixelformat=RG10 \
        --stream-mmap --stream-count=100 -d $camera_num