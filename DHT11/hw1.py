import Adafruit_DHT
import time
import LED
import sys, pygame



sensor = Adafruit_DHT.DHT11

GPIO = 14
theLED = 0
pygame.init()
pygame.mixer.music.load("beep.mp3")

try:
    while True:
        LED.Setup(10, "OUT")
        LED.Setup(5, "OUT")
        LED.Setup(13, "OUT")
        currentTime = time.strftime("%H:%M:%S")


        humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)

        if temperature is not None:
            print(currentTime,'-> Temp={0}*C '.format(temperature))

            if(temperature>=31):
                if theLED>0:
                    LED.TurnOffLED(theLED)
                theLED = 13
                LED.TurnOnLED(13)
                pygame.mixer.music.play(5)
            elif temperature>=27 and temperature<=30:
                if theLED>0:
                    LED.TurnOffLED(theLED)
                theLED = 5
                LED.TurnOnLED(5)
            elif temperature>=20 and temperature<=26:
                if theLED>0:
                    LED.TurnOffLED(theLED)
                theLED = 10
                LED.TurnOnLED(10)


        else:
            print('Failed to get reading. Try again!')

        time.sleep(5)
except:
    GPIO.cleanup()
