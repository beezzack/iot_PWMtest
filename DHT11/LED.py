import RPi.GPIO as GPIO
def Setup(GPIOnum, OUT_IN):
    GPIO.setmode(GPIO.BCM)

    if OUT_IN == "OUT":
        GPIO.setup(GPIOnum, GPIO.OUT)
        GPIO.output(GPIOnum, False)
    else:
        GPIO.setup(GPIOnum, GPIO.IN)
def TurnOnLED(GPIOnum):
    GPIO.output(GPIOnum, True)

def TurnOffLED(GPIOnum):
    GPIO.output(GPIOnum, False)
