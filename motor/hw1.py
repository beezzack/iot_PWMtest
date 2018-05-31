import RPi.GPIO as GPIO
import time
import LED
from time import sleep

    


counter = 0
def SetAngle(angle):
    dutyCycle = 1/20 * angle + 3
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.5)
def motion(GPIOnum):
    global counter

    if GPIO.input(GPIOnum):
        counter += 1
        LED.TurnOnLED(4)
        print("Motion detected{0}".format(counter))
        pwm.stop()

    else:
        LED.TurnOffLED(4)
        print("Motion not detected")
        pwm.start(0)

        


if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        pwm=GPIO.PWM(17, 50)
        pwm.start(0)
        LED.Setup(4,"OUT")
        GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.add_event_detect(14, GPIO.BOTH, callback = motion, bouncetime = 300)
        while True:
            SetAngle(90)
            SetAngle(180)
            SetAngle(0)
            

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
