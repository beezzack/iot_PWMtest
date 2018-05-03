import RPi.GPIO as GPIO
import time
import LED


def turnOnOffLED(GPIOpin, LDR_DO):
    if LDT_DO == 1:
        return True;
    else:
        return False;

def setup(GPIOnum):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOnum, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


counter = 0

def motion(GPIOnum):
    global counter
    if turnOnOffLED(26) == True:
        print("NOT LIGHT")
        if GPIO.input(GPIOnum):
            counter += 1
            LED.TurnOnLED(2)
            print("Motion detected{0}".format(counter))

        else:
            LED.TurnOffLED(2)
            print("Motion not detected")
    else:
        print("LIGHT")


try:
    LED.Setup(2,"OUT")
    setup(14)
    GPIO.add_event_detect(14, GPIO.BOTH, callback = motion, bouncetime = 150)
    while True:
        time.sleep(1)

except :
    GPIO.cleanup()
