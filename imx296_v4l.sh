#!/usr/bin/sh

 v4l2-ctl --set-fmt-video=width=1440,height=1080,pixelformat=RG10 --stream-mmap --stream-count=100 -d /dev/video0