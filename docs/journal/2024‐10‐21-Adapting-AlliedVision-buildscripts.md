# tl;dr

I cribbed an existing [Allied Vision package](https://github.com/alliedvision/alvium-jetson-driver-release) for building custom modules for Jetpack 6, added the [Vision Components](https://github.com/VC-MIPI-modules/vc_mipi_nvidia) module source, and updated the code for Jetpack 6.1 / L4T-36.4.

To get started, see [the README in the l4t-36.4.0 branch](https://github.com/amarburg/vc-jetson-driver-release/tree/l4t-36.4.0/alpha).

As of right now, it _does_ build the modules, but I am not sure of the cleanest way to deploy.   It does not build the `.dtbo` but soon.... 

Based on past experience, I'm looking for a deploy path that lets me update in userspace (upgrading the kernel modules and DTBOs on a running system), rather than building a pristine filesystem to flash onto an empty system.  It's a much faster dev cycle.

# Details

My previous projects have used Allied Vision CSI-2 cameras under Jetpack 4.x/5.x.  As such I've become fairly comfortable with the [Allied Vision repo](https://github.com/amarburg/linux_nvidia_jetson) which combines custom kernel source with helper scripts for building and packaging the kernel.

For this project, we are targeting Jetpack 6.x on an Orin Nano baseboard, and as a first step we're interested in integrating the [Vision Components MIPI driver](https://github.com/VC-MIPI-modules/vc_mipi_nvidia).

Just for familiarity, I decided to start with the [Allied Vision driver package for Jetpack 6.x](https://github.com/alliedvision/alvium-jetson-driver-release).  It turns out it's not quite as mature as the Jetpack 5.x package -- it doesn't automatically managed deployment -- but it still provided a starting point.

Jetpack 6.x now uses out-of-tree (OOT) module builds which lets you build kernel modules without having to build the full kernel.  The OOT kernel module source can be found in the Jetpack ["public_sources"](https://developer.nvidia.com/embedded/jetson-linux-r3640) at `Linux_for_Tegra/sources/kernel_oot_modules_src.tbz2`.   The "stock" NVidia source includes four separate trees: `nvidia-nvgpu`, `nvidia-nvethernetrm`, `nvidia-hwpm` and `nvidia-oot`.

The Allied Vision package is essentially a meta-repo which includes each of those four trees as a sub-module.   The `nvidia-oot` submodule then includes [AVT's custom changes](https://github.com/alliedvision/nvidia-oot) to the video modules.   I don't think the Allied copies of the other three trees are modified from Nvidia's upstream.  At the top level they also include [Allied's custom driver](https://github.com/alliedvision/alvium-csi2-driver) as a separate directory.

AVT then includes a top-level makefile and instructions for building everything.

## Adapting for Vision Components

Adapting the Vision Components was a two-step process:

0. The latest AVT repo is for Jetpack 6.0 / l4t-36.3.0.   We're using Jetpack 6.1 / l4t-36.4.0, so forward-port the module source to the latest version.
1. Integrate the Vision Components modules as a separate OOT directory, following the pattern established by the `alvium-csi2-driver` directory.

### 0. Set up my own version of the nvidia-oot Repo

AVT includes a submodule `nvidia-oot` which contains their customized version of the nvidia-oot tree ... it's largely light modifications to the video handling code.

For our purposes, fork a [copy of the AVT nvidia-oot](https://github.com/amarburg/nvidia-oot).

The branches:

* `l4t/l4t-r36.3-avt/main` is the R36.3 code from Allied Vision.
* `nvidia/l4t-r36.3` is the "pristine" code from R36.3 (synced from their [git repo](https://nv-tegra.nvidia.com/r/linux-nv-oot.git) branch "l4t/l4t-r36.3")
* `nvidia/l4t-r36.4` is the "pristine" code from R36.4 (synced from their [git repo](https://nv-tegra.nvidia.com/r/linux-nv-oot.git) branch "l4t/l4t-r36.4")

Then

* `vc/l4t-r36.4` is the `nvidia/l4t-r36.4` branch with _most_ of the [branches from VC](https://github.com/VC-MIPI-modules/vc_mipi_nvidia/tree/master/patch/kernel_Xavier_36.2.0%2B) applied.   Didn't apply the patches which touch Makefiles.  Note this branch _does not_ include the AVT changes from `l4t/l4t-r36.3-avt/main``

Updated the submodule in [my repo](https://github.com/amarburg/vc-jetson-driver-release) to point to this branch in my `nvidia-oot`.

I also reverted all of the other submodules to point to the upstream Git repo at Nvidia.  I didn't see the point in using Allied vision's forks of those repos.

### 1. Copy in VC source

By apeing  `alvium-csi2-driver`, create a `vc-mipi-driver` directory which includes the [VC source code](https://github.com/VC-MIPI-modules/vc_mipi_nvidia/tree/master/src).

Once done, remove the `alvium-csi2-driver` submodule.

