import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import math
import LED, PIR
import sys, pygame

sensor = Adafruit_DHT.DHT11

#溼度sensor
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

        humidity, temperature = Adafruit_DHT.read_retry(sensor, 14)#sensor
        dewpoint = Dewpoint(temperature,humidity)
        heatstrokeCoef = HeatstrokeCoefficient(temperature, humidity)

        if humidity is not None and temperature is not None:
            print(currentTime, '-> HeatstrokeCoef={0} Dewpoint={1:0.1f}'.format(heatstrokeCoef, dewpoint))
            if heatstrokeCoef >= 40:
                GPIO.add_event_detect(22, GPIO.BOTH, callback=motion, bouncetime=200)
                for num in (1,4):
                    LED.TurnOnLED(13)
                    time.sleep(0.5)
                    LED.TurnOffLED(13)
                    time.sleep(0.5)
                GPIO.remove_event_detect(22)
                
            elif heatstrokeCoef >=35 and heatstrokeCoef <= 39:
                GPIO.add_event_detect(22, GPIO.BOTH, callback=motion, bouncetime=200)
                LED.TurnOnLED(13)
                time.sleep(4)
                LED.TurnOffLED(13)
                GPIO.remove_event_detect(22)
                
            elif heatstrokeCoef >=30 and heatstrokeCoef <= 34:
                LED.TurnOnLED(5)
                time.sleep(4)
                LED.TurnOffLED(5)
                
            elif heatstrokeCoef <= 29:
                LED.TurnOnLED(10)
                time.sleep(4)
                LED.TurnOffLED(10)
        else:
            print('Failed to get reading. Try again')
        time.sleep(5)
except(KeyboardInterrupt):
    GPIO.cleanup()
finally:
    GPIO.cleanup()
