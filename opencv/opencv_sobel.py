#!/usr/bin/env python3
#
# Sample script which uses OpenCV to read images from one camera,
# then runs some basic image processing ... Gaussian blue and Sobel edges.
# It tries to display on the screen, this script should be run _on the nano_
#

import cv2

if __name__ == "__main__":

    # Camera 0 is "left", camera 1 is "right"
    camera_num = 0

    # This is fixed for these cameras
    image_size = (1080,1440)
    framerate = 10

    # GStreamer string, may be possible to optimize this further?
    gst_string = f'nvarguscamerasrc sensor-id={camera_num} wbmode=0 aelock=true ispdigitalgainrange="1 8" gainrange="1 48" exposuretimerange="35000 100000000" ! video/x-raw(memory:NVMM),width={image_size[1]},height={image_size[0]},framerate={framerate}/1 ! nvvidconv ! queue ! video/x-raw,pixel-format=(string)BGR ! gamma gamma=0.7 ! videobalance brightness=0.2 !  videoconvert ! video/x-raw,pixel-format=(string)BGR ! appsink'
        
    print(f"Using GStreamer configuration: {gst_string}")

    # Open OpenCV camera
    camera = cv2.VideoCapture(gst_string, cv2.CAP_GSTREAMER )

    if camera.isOpened() is False:
        print("Could not open camera")
        exit()

    print(f"Camera open using backend: {camera.getBackendName()}")

    # Read the actual properties from the OpenCV VideoCapture (should agree with above)
    cap_width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap_height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cap_fps = camera.get(cv2.CAP_PROP_FPS)

    print(f"OpenCV VideoCapture: input images {cap_width} x {cap_height} as {cap_fps} FPS")

    while True:

        success, img = camera.read()

        if success is False:
            print("no image")
            continue

        # Show the "original" image
        cv2.imshow("original image", img)
        
        # Shrink the image by a factor of 2 in both axes
        downsampled = cv2.resize(img, dsize=(0,0), fx=0.5, fy=0.5)

        # Perform Gaussian blur
        blurred = cv2.GaussianBlur(downsampled, ksize=(0,0), sigmaX=7 )
        cv2.imshow("blurred", blurred)

        # Perform Sobel edges on blurred images
        sobel = cv2.Sobel(blurred, ddepth=cv2.CV_8U, dx=1, dy=1, ksize=3)
        cv2.imshow("sobel", sobel)

        cv2.waitKey(1)
