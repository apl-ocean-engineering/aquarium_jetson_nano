I've found the Nano install process to be somewhat unstable.   This is the latest working process for me.

At present, using [L4T-36.4.3](https://docs.nvidia.com/jetson/archives/r36.4.3/DeveloperGuide/index.html) and [Jetpack 6.2](https://developer.nvidia.com/embedded/jetpack-sdk-62).

We install to the onboard NVMe. 

# Install Jetpack

Out of the box, I was not able to install to the Nano.  It would get partway through the process but not be able to connect to the NFS server on the Ubuntu install host running SDK Manager.


Follow the instructions from the [NVidia Developer's guide](https://docs.nvidia.com/jetson/archives/r36.4.3/DeveloperGuide/IN/QuickStart.html#to-flash-the-jetson-developer-kit-operating-software).  Specifically:

1. Install the Linux-tegra SDK
2. Put the Jetson into developer's mode:
3. Then, to flash to "Super" mode with NVMe:

```
$ sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 \
  -c tools/kernel_flash/flash_l4t_t234_nvme.xml -p "-c bootloader/generic/cfg/flash_t234_qspi.xml" \
  --showlogs --network usb0 jetson-orin-nano-devkit-super internal
```


# Install OOT camera driver and device tree