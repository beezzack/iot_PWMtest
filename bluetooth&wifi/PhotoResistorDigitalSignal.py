import RPi.GPIO as GPIO

def SetupPhotoresistor(GPIOpin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOpin,GPIO.IN)
