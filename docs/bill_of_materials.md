# Bill of Materials

For reference, here's our bill of materials:

| P/N | Description |
|-----|-------------|
|     | Jetson Orin Nano dev kit |
|     | NVMe SSD (various) |
| VC [MIPI IMX296C](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-IMX296C?qs=sGAEpiMZZMt82OzCyDsLFNIe%252BVGQS%252Bz169bx8A5SVck%3D) | Two Vision Components IMX296C modules |
| VC [MIPI FPC 200/22-22](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-FPC-cable-200-22-22?qs=Znm5pLBrcAJnSTxvCpPa%2FQ%3D%3D) | Two 200mm 22pin-22pin MIPI cables |
| VC [MIPI LHLD12](https://www.mouser.com/ProductDetail/Vision-Components/MIPI-LHLD12?qs=Znm5pLBrcAJI2%252BzumslyRA%3D%3D) | Two M12 lens holders |
| Raspberry Pi [SC0947](https://www.mouser.com/ProductDetail/Raspberry-Pi/SC0947?qs=rQFj71Wb1eVOORb%252B17NIKQ%3D%3D) | Two M12 Lens, 15 Megapixel, 2.7mm, wide angle lens - -185 deg FOV.  **NOTE:** The Mouser link is for a **10 pack** of lenses.   It's a great deal!! |
| | *Housing includes* |
|  | One BlueRobotics 4" acrylic tube -- we used old non-locking style as it lets us get the length exactly right.  You should be able to replicate with locking 4" housings but the packaging will not be as effiecient (the whole system will be longer) |
|  | Two Bluerobotics non-locking 4" flanges |
| BlueRobotics [BR-102993-998](https://bluerobotics.com/store/watertight-enclosures/locking-series/wte-end-cap-vp/) | 4" Acrylic endcap |
|  BlueRobotics [BR-102993-999](https://bluerobotics.com/store/watertight-enclosures/locking-series/wte-end-cap-vp/) | 4" Aluminum endcap.  We purchased a blank (no holes) endcap and drilled two M10 holes.  Could also use the 5 x M10 endcap with appropriate blanking plugs. |
|  BlueRobotics [BR-100783](https://bluerobotics.com/store/watertight-enclosures/enclosure-tools-supplies/vent-asm-r1/) | Vent plug |
| BlueRobotics [BR-100897](https://bluerobotics.com/store/cables-connectors/pur-subsea-cable/) | PUR Ethernet+Power cable.  We use about 50cm from the camera to the ROV. |
|  BlueRobotics [M10-7.5-LC  BR-100870-075](https://bluerobotics.com/store/cables-connectors/penetrators/wlp-vp/?attribute_bulkhead-size-seal-size-plug-compression-compatible-cable-diameter=M10+-+7.5+mm+-+LC+-+7.5+mm+%C2%B1+0.3+mm) | Wetlink penetrator  M109-7.5-LC |
| BlueRobotics [BR-100434-010](https://bluerobotics.com/store/cables-connectors/wlp-blank/) | M10 Blank (if needed) |
| | *Custom leak detector board which includes:* |
| Adafruit [4900](https://www.adafruit.com/product/4900) |  QtPy RP2040 |
| Adafruit [2652](https://www.adafruit.com/product/2652) |  BME280 module |
| Adafruit [4399](https://www.adafruit.com/product/4399) |  Stemma QT cable  |
| Blue Robotics [BR-100954](https://bluerobotics.com/store/sensors-cameras/leak-sensor/sos-probes/) |  SOS Probes 6" |
| | *To fit everything in the 4" housing I needed to use:* |
| [Amazon link](https://www.amazon.com/MEETOOT-Network-Connector-Ethernet-Unshielded/dp/B09PD82G2D/ref=sr_1_3?crid=1CK54HTWFALQ4&dib=eyJ2IjoiMSJ9.4te905jfYoaSKUxD8zTB9ERNZ6HWF7-1xrOnCX0voLt4fEsVihKT5lSGrxE4p5raS4LQtjq4jEBEIvNmBe4J-JHku6w4uHqgzYUxQJhWWmvWvHjA2tcQj7pJg5cOgR_tilbnXnN9xfrNn8ueffafe7LpvKry_xrGl78FPP6phds8wasjdi6TDLoiAznXGYpMRdYV_gVI3B2ZxqaurzWPbNGRDvyf6rXdlYjnpJyJwNc.fXVHnF1Y3OcMfysnD-DlpcZReV3BYK67GfyotcVnT4s&dib_tag=se&keywords=short+rj45&qid=1744484089&sprefix=short+rj%2Caps%2C205&sr=8-3) | "Shorty" RJ45 plugs |
| [AliExpress](https://www.aliexpress.us/item/3256803341065609.html?spm=a2g0o.order_list.order_list_main.4.505b1802y2obiQ&gatewayAdapt=glo2usa) | Low-profile right-angle USB-A cables.  This is an example part I had from another project, you could get a direct USB-A to USB-C for the QtPy. |

The unit shown above also contains a number of laser cut and 3D printed parts.   STLs and drawings forthcoming.
