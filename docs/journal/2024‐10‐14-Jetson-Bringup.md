Unpacked the Jetson Nano and set it up.   Installed a ~~16GB~~ (see below, probably need a 32GB card, even with root on NVMe) SD card and 128GB NVMe SSD.

Notes:
* This is Jetson Orin Nano 8GB with SD card slot (P3767-0005) mounted to Jetson Orin Nano Developer Kit (P3766)

Also set up PI global camera with C-mount lens and tripod.  Connected to "CAM0" port on Nano with "Raspberry Pi 5" camera cable (large 15-pin connector to small 22-pin connector)

![IMG_0435](https://github.com/user-attachments/assets/57dd7258-9c79-4fad-9eaa-e0c6d53cedf6)

# Install Jetpack

* Start NVidia [SDK Manager](https://developer.nvidia.com/sdk-manager).  
* Put jumper on pins 10-11 on Button header (J14) to put in recovery mode
* Connect 3v3 TTL serial port to 3-4-7 on Button header (J14) to get serial console
* Nano detected by SDK Manager
* Install Jetpack 6.1 with NVMe as primary storage.   
* Use "Manual" install mode since it's already in Recovery mode (via pin header)

![image](https://github.com/user-attachments/assets/4c1b56c3-eef0-4b39-8d18-dacddef7088d)

Hm, initial install failed.  Try 32GB SD card in case it's running out of space (I wouldn't think space was an issue if it's installing the OS to the NVMe but you never know)....

Try a different USB-C cable.   Problems persist trying to flash from Jetpack.  May try "SD Card" method?

Hm, this time it actually installs a bootable system.   Not sure if it's the USB-C cable or the larger SD card.

Complete installation over SSH ... I provide the IP address to SDK manager over ethernet, I'm sure you could also use the USB-network connection.

![Screenshot from 2024-10-14 12-06-55](https://github.com/user-attachments/assets/e41e43a2-a92d-4c62-84a1-900022760288)

Let it install all of the NVidia goodies. 

That seemed to work.

# Arducam driver

Try to follow [Arducam quickstart](https://docs.arducam.com/Nvidia-Jetson-Camera/Native-Camera/Quick-Start-Guide/#12mp-imx708-camera)

Unfortunately, not available for Jetpack 6.1:

```
Cannot find the corresponding deb package, please send the following information to support@arducam.com
Kernel version:  5.15.148-tegra-36.4.0-20240912212859
Jetson type:  NVIDIA Jetson Orin Nano Developer Kit
```

... there is a release for L4T 36.4.0 which is ...close?
 
<img width="1085" alt="image" src="https://github.com/user-attachments/assets/1d302e9e-c9f3-418d-8f7b-dfdc3e1fb6ed">



