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
    gst_string = "nvarguscamerasrc sensor-id={camera_num} ! video/x-raw(memory:NVMM),width={image_size[1]},height={image_size[0]},framerate={framerate}/1 ! nvvidconv ! queue ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink"

    # Open OpenCV camera
    left = cv2.VideoCapture(gst_string.format(camera_num=0, image_size=image_size, framerate=framerate), cv2.CAP_GSTREAMER )
    right = cv2.VideoCapture(gst_string.format(camera_num=1, image_size=image_size, framerate=framerate), cv2.CAP_GSTREAMER )

    if left.isOpened() is False:
        print("Could not open left camera")
        exit()

    if right.isOpened() is False:
        print("Could not open right camera")
        exit()

    while True:

        # Use grab() to trigger an acquisition
        #  https://docs.opencv.org/4.11.0/d8/dfe/classcv_1_1VideoCapture.html#ae38c2a053d39d6b20c9c649e08ff0146
        #
        left.grab()
        right.grab()

        # ... then retrieve to retrieve the data from the camera
        #  https://docs.opencv.org/4.11.0/d8/dfe/classcv_1_1VideoCapture.html#a9ac7f4b1cdfe624663478568486e6712
        #
        left_success, left_img = left.retrieve()
        right_success, right_img = right.retrieve()

        if left_success is False or right_success is False:
            print("no image")
            continue

        # Shrink both images
        left_downsampled = cv2.resize(left_img, dsize=(0,0), fx=0.5, fy=0.5)
        right_downsampled = cv2.resize(right_img, dsize=(0,0), fx=0.5, fy=0.5)

        # Composite the two images side-by-side
        left_sz = left_downsampled.shape
        right_sz = right_downsampled.shape

        composite = numpy.zeros( (max(left_sz[0],right_sz[0]),left_sz[1]+right_sz[1],3), dtype=left_img.dtype )

        # This is a copy, so it's not terribly efficient
        composite[0:left_sz[0], 0:left_sz[1],:] = left_downsampled
        composite[0:right_sz[0], left_sz[1]:left_sz[1]+right_sz[1],:] = right_downsampled

        cv2.imshow("left", left_downsampled)
        cv2.imshow("right", right_downsampled)

        cv2.imshow("stereo", composite)
        cv2.waitKey(1)
