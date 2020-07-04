import Adafruit_DHT
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,27) #GPI027
    print("Humidity = {} %; Temperature = {} C".format(humidity,temperature))