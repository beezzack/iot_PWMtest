import RPi.GPIO as GPIO
def setup_PIR(GPIOnum):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOnum, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
