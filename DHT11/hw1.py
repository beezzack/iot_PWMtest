import Adafruit_DHT
import time
import LED


sensor = Adafruit_DHT.DHT11

GPIO = 14

while True:
    LED.setup(10, "OUT")
    LED.Setup(5, "OUT")
    LED.Setup(13, "OUT")



    humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)

    if temperature is not None:
        print(currentTim,'-> Temp={0}*C '.format(temperature))

        if(temperature>=31):
            LED.TurnOnLED(13)
            time.sleep(1)
            LED.TurnOffLED(13)
            time.sleep(1)
        else if(temperature>=27 and temperature<=30):
            LED.TurnOnLED(5)
            time.sleep(1)
            LED.TurnOffLED(5)
            time.sleep(1)
        else if(temperature>=20 and temperature<=26):
            LED.TurnOnLED(13)
            time.sleep(1)
            LED.TurnOffLED(13)
            time.sleep(1)


    else:
        print('Failed to get reading. Try again!')

    time.sleep(5)
