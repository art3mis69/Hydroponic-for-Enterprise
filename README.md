# Hydroponic-for-Enterprise


## Raspberry Pi: Measure Humidity and Temperature with DHT11 ##

With the Raspberry Pi and some sensors, it is easy to measure the temperature without much effort. In addition, however, the humidity in certain situations or projects (such as a weather station) can be enlightening. Sensors such as the DHT11 and DHT22 are not only available for a few euros, but they can also measure the temperature as well as the humidity.

## Accessories ##

As the sensors already carry (almost) everything,not many additional accessories are required. I have used this:

*DHT11 humidity sensor
*Jumper wires
*Ethernet Cable
*USB Power Cable

## Setup of Raspberry Pi Humidity Sensor ##

![alt text](https://github.com/art3mis69/Hydroponic-for-Enterprise/blob/master/DHT11_GPI.png)

The left pin of the sensor is connected to 3V3 of Pi (pin1), the second sensor pin is connected (GPIO4, pin7) and the right senior pin comes at GND (Pin6) from the Pi. The second pin from the right of the sensor remains free.Resistor,BreadBoard is not necessary.

## Raspberry Pi Humidity Software Installation and Testing ##

First of all, some packages have to be installed:
```
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl git
```

Now the library for the sensors can be loaded. I use a pre-built Adafruit library that supports a variety of sensors:
```
git clone https://github.com/art3mis69/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
sudo python setup.py install
```

This creates a Python library that we can easily integrate into our projects.

If everything went well, we can already read the temperature and humidity. The easiest way is to first use the demo files:
```
cd examples
sudo ./AdafruitDHT.py 11 4
```

The first parameter (11) indicates which sensor was used and the second, to which GPIO it is connected (not the pin number, but the GPIO number). This produces an output like the following:
```
$ sudo ./AdafruitDHT.py 11 4
Temp=24.0*  Humidity=41.0%
```

__Attention: The sensors are only ready every two seconds. Be careful not to start a query every second.__

To integrate the Raspberry Pi humidity library into other (Python) projects, you only need the following:
```
import Adafruit_DHT
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,27) #GPI027
    print("Humidity = {} %; Temperature = {} C".format(humidity,temperature))
```

##Output

!![alt text](https://github.com/art3mis69/Hydroponic-for-Enterprise/blob/master/DHT11sensor_output.png)



