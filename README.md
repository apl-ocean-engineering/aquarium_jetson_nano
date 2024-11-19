# aquarium_jetson_nano

Scratchpad repo for exchanging code and ideas during Jetson Orin Nano testing for Seattle Aquarium BlueROV project.

For now, see the [wiki](https://github.com/apl-ocean-engineering/aquarium_jetson_nano/wiki)

# Trigger information

On the Orin NX devboard:

| Jetson Signal | Jetson Pin | GPIO Pin | VC Pin |
|---------------|------------|----------|--------|
| CAM0_PWDN | 114 | GPIO3_PH.06 | gpiochip0.49 | Trigger to sensor |
| CAM0_MCLK | 116 | |  | Flash from sensor |
| CAM1_PWDN | 120 | GPIO3_PAC.00 | gpiochip0.138 | Trigger to sensor |
| CAM1_MCLK | 122 | | | Flash from sensor |