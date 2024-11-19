#!/usr/bin/bash
#
# Stream data from one camera using v4l2
#

WHICH_CAMERA=0

. imx296_constants.sh

 v4l2-ctl --set-fmt-video=width=$IMG_WIDTH,height=$IMG_HEIGHT,pixelformat=RG10 \
        --stream-mmap --stream-count=180 -d $WHICH_CAMERA