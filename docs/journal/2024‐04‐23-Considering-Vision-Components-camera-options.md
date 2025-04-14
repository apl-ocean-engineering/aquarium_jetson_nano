We've looking at camera modules from [Vision Components](https://www.google.com/search?client=safari&rls=en&q=vision+components&ie=UTF-8&oe=UTF-8).  They appear relatively inexpensive and a subset are available on Mouser.

It should be mentioned we came on VC somewhat randomly ... looking for Jetpack support for the IMX296 sensor on the Raspberry Pi [Global Shutter (GS)](https://www.raspberrypi.com/documentation/accessories/camera.html) camera.   If we're just looking for a low-cost camera sensor for Jetson we could should troll the list of [Jetson Supported Cameras](https://developer.nvidia.com/embedded/jetson-partner-supported-cameras).

Info from Mouser and this [VC MIPI Module datasheet](https://www.mipi-modules.com/fileadmin/external/documentation/hardware/VC_MIPI_Camera_Module/index.html)

In any case, these are the VC camera modules generally in stock at Mouser:

- "Starvis" is Sony's line of low-light rolling shutter cameras for e.g. CCTV
- "Pregius" is Sony's line of global shutter cameras

| Price | Sensor | Res. | Shutter | Notes |
|-------|--------|------|---------|-------|
| $82 | [OV9281](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-OV9281?qs=Znm5pLBrcALsMIfZR1kfbw%3D%3D) | 1280 x 800 @ 120fps | Global | |
| $833 | [IMX250](https://www.mouser.com/ProductDetail/Vision-Components/VC-MIPI-IMX250?qs=t7xnP681wgXFIrIX%252B2h6wQ%3D%3D) | 2448 x 2048 @ 101fps | Global |  Pregius |
| $551 | [IMX252C](https://www.mouser.com/ProductDetail/Vision-Components/VC-MIPI-IMX252C?qs=t7xnP681wgXs%252BjQMpPBb7Q%3D%3D) | 2048 x 1536 @ 151fps | Global | Pregius |
| $190 | [IMX290](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-IMX290?qs=Znm5pLBrcAJt1hUiCw5TOw%3D%3D) | 1920 x 1080 @ 120fps | Rolling | Starvis |
| $150 | [IMX296](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-IMX296?qs=Znm5pLBrcALfpja0UWCKMw%3D%3D) [IMC296C](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-IMX296C?qs=Znm5pLBrcAJOFFaly5djSA%3D%3D) | 1440 x 1080 @ 60fps | Global | Pregius |
| $115 | [IMX327C](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-IMX327C?qs=Znm5pLBrcAJpeYGEaC2%2FCQ%3D%3D) | 1920 x 1080 @60fps | Rolling | Starvis |
| $160 | [IMX335](https://www.mouser.com/ProductDetail/Vision-Components/VC-MIPI-IMX335?qs=t7xnP681wgW3%2FKOoKnRjcw%3D%3D) [IMX335C](https://www.mouser.com/ProductDetail/Vision-Components/VC-MIPI-IMX335C?qs=t7xnP681wgWTNtGcOob61Q%3D%3D) | 2560 x 1964 @ 60fps | Rolling | Starvis |
| $200 | [IMX412C](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-IMX412C?qs=Znm5pLBrcALkFJPOGJOC0Q%3D%3D) | 4056 x 3040@40fps | Rolling | Starvis |
| $190 | [IMX415C](https://www.mouser.com/ProductDetail/Vision-Components/VC-MIPI-IMX415C?qs=t7xnP681wgXy0NWbUYQoyQ%3D%3D) | 3840 x 2160 @ 60fps| Rolling | Starvis |

Note we will also need a lens holder:

* [M12 holder](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-LHLD12?qs=Znm5pLBrcAJI2%252BzumslyRA%3D%3D)
* [CS/C holder](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-LHLDCM?qs=Znm5pLBrcAK0BV9ne6WpWQ%3D%3D)

And likely some cables.