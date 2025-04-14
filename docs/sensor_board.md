The Nano contains a small sensor board which samples the environment in the housing.   It consists of an Adafruit [QtPy M0](https://www.adafruit.com/product/4600), an [Adafruit BME280](https://www.adafruit.com/product/2652) module, an a custom driver circuit board for two [BlueRobotics SOS Leak sensors](https://bluerobotics.com/store/sensors-cameras/leak-sensor/sos-probes/)

The board runs this [Circuitpython script (in this repo)](../qtpy_firmware/).   This firmware samples all sensors a 1Hz and produces a JSON string:

```
{"temperature": 39.7,"humidity": 28.1,"pressure": 1018.2,"altitude": -40.52,"leak": { "leak0_voltage": 0.01, "leak1_voltage": 0.00}}
```

* `temperature` is in degree C
* `humidity` is in %
* `pressure` is in hPa
* `altitude` is in meters
* `leak*_voltage` is in volts, with one for each leak sensor.   Voltages near 0 mean "no leak."  Voltages > 1.0 - 3.3 mean "leak!!"

