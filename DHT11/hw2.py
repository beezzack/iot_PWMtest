import Adafruit_DHT
import time
import math
import LED, PIR
import sys, pygame

sensor = Adafruit_DHT.DHT11

GPIO = 14#溼度sensor
pygame.init()
pygame.mixer.music.load("beep.mp3")

def HeatstrokeCoefficient(celsius, humidity):
    heatstrokeCoefficient = celsius + humidity * 0.1
    return heatstrokeCoefficient

def Dewpoint(celsius, humidity):
    a = 17.271
    b = 237.7
    temp = (a * celsius)/(b + celsius)+math.log(humidity/100)
    td = (b*temp)/(a-temp)
    return td
def motion(channel):
    print("Motion detected ")
    pygame.mixer.music.play(3)

try:
    LED.Setup(10, "OUT")#G
    LED.Setup(5, "OUT")#Y
    LED.Setup(13, "OUT")#R
    PIR.setup_PIR(22)#PIR
    while True:
        currentTime = time.strftime("%H:%M:%S")

        humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)
        dewpoint = Dewpoint(temperature,humidity)
        heatstrokeCoef = HeatstrokeCoefficient(temperature, humidity)

        if humidity is not None and temperature is not None:
            print(currentTime, '-> HeatstrokeCoef={0} Dewpoint={1:0.1f}'.format(heatstrokeCoef, dewpoint))
            if heatstrokeCoef >= 40:
                GPIO.add_event_detect(22, GPIO.BOTH, callback=motion, bouncetime=200)
                for num in (1,4):
                    TurnOnLED(13)
                    sleep(0.5)
                    TurnOffLED(13)
                    sleep(0.5)
                GPIO.remove_event_detect(22)
            elif heatstrokeCoef >=35 and heatstrokeCoef <=39:
                GPIO.add_event_detect(22, GPIO.BOTH, callback=motion, bouncetime=200)
                TurnOnLED(13)
                sleep(4)
                TurnOffLED(13)
                GPIO.remove_event_detect(22)
            elif heatstrokeCoef >=30 and heatstrokeCoef <=34:
                TurnOnLED(5)
                sleep(4)
                TurnOffLED(5)
            elif heatstrokeCoef <= 29:
                TurnOnLED(10)
                sleep(4)
                TurnOffLED(10)
        else:
            print('Failed to get reading. Try again')
        time.sleep(5)
except:
    GPIO.cleanup()
