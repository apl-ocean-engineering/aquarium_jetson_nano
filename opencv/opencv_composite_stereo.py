#!/usr/bin/env python
#
# Sample script which uses OpenCV to read images from both cameras
#
# It tries to display on the screen, this script should be run _on the nano_
#
# Note that the two cameras are free running so there will be a lag between the two
# images.   There are a variety of ways to address this.

import cv2
import numpy

if __name__ == "__main__":

     # This is fixed for these cameras
    image_size = (1080,1440)
    framerate = 30

    # GStreamer string, may be possible to optimize this further?
    gst_string = '''
nvarguscamerasrc sensor-id=0 wbmode=1 ispdigitalgainrange=\"1 8\" gainrange=\"1 48\" tnr-mode=0 exposuretimerange="2000 20000000" saturation=1.3 name=left 
nvarguscamerasrc sensor-id=1 wbmode=1 ispdigitalgainrange=\"1 8\" gainrange=\"1 48\" tnr-mode=0 exposuretimerange="2000 20000000" saturation=1.3 name=right
glstereomix name=mix 
left. ! video/x-raw(memory:NVMM),width={image_size[1]},height={image_size[0]},framerate={framerate}/1 ! nvvidconv ! video/x-raw ! glupload  ! mix.
right. ! video/x-raw(memory:NVMM),width={image_size[1]},height={image_size[0]},framerate={framerate}/1 ! nvvidconv ! video/x-raw ! glupload ! mix. 
mix. ! video/x-raw(memory:GLMemory),multiview-mode=side-by-side  ! glcolorconvert ! gldownload ! 
        queue ! video/x-raw,format=BGRx  ! videoconvert ! video/x-raw,format=BGR ! appsink'
'''

# ! glcolorbalance constrast=0.1 brightness=0.2 saturation=1.2

    gst_string = gst_string.format(image_size=image_size, framerate=framerate)
    print(gst_string)

    # Open OpenCV camera
    stereo = cv2.VideoCapture(gst_string, cv2.CAP_GSTREAMER )

    if stereo.isOpened() is False:
        print("Could not open camera")
        exit()

    while True:

        success, img = stereo.read()

        if success is False:
            print("no image")
            continue

        # Shrink both images
        downsampled = cv2.resize(img, dsize=(0,0), fx=0.5, fy=0.5)

        cv2.imshow("stereo", downsampled)
        cv2.waitKey(1)
