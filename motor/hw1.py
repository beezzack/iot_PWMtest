import RPi.GPIO as GPIO
import time
import LED
from time import sleep

def setup(GPIOnum):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOnum, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


counter = 0
def SetAngle(angle):
    dutyCycle = 1/20 * angle + 3
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(1)
def motion(GPIOnum):
    global counter

    if GPIO.input(GPIOnum):
        counter += 1
        LED.TurnOnLED(4)

        print("Motion detected{0}".format(counter))

    else:
        LED.TurnOffLED(4)
        while True:
            SetAngle(90)
            SetAngle(180)
            SetAngle(90)
            SetAngle(0)
        print("Motion not detected")


if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(3, GPIO.OUT)
        pwm=GPIO.PWM(3, 50)
        pwm.start(0)
        LED.Setup(4,"OUT")
        setup(12)
        GPIO.add_event_detect(12, GPIO.BOTH, callback = motion, bouncetime = 150)


    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
