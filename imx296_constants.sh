#
# Constant values for the IMX296, used by multiple scripts
#

IMG_WIDTH=1440
IMG_HEIGHT=1080
IMG_RATE=30

# Flags to pass to nvarguscamerasrc 
NVARGUS_CONFIG="wbmode=0 aelock=true ispdigitalgainrange=\"1 8\" gainrange=\"1 48\""

configure_cameras() {
    for camera_num in "$@"; do
        v4l2-ctl -d $camera_num -c bypass_mode=0 -c override_enable=1
    done
}