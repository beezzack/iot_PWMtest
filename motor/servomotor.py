im[prt RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
pwm = GPIO.PWM(3,50)
pwm.start(0)
GPIO.output(3, True)

def SetAngle(angle)
    dutyCycle= 1/20 * angle + 3
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(1)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()

SetAngle(180)
