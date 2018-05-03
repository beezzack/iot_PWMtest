import RPi.GPIO as GPIO
import time
import LED

def SetupPhotoresistor(GPIOpin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOpin,GPIO.IN)
    
def turnOnOffLED(GPIOpin, LDR_DO):
    if LDR_DO == 1:
        print("Dark")
        LED.TurnOnLED(GPIOpin)
    else:
        print("light")
        LED.TurnOffLED(GPIOpin)

def setup(GPIOnum):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOnum, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


counter = 0

def motion(GPIOnum):
    global counter
    if GPIO.input(GPIOnum):
        counter += 1
        turnOnOffLED(2,GPIO.input(26))
        print("Motion detected{0}".format(counter))

    else:
        print("Motion not detected")
    

if __name__ == "__main__":
    LED.Setup(2,"OUT")
    SetupPhotoresistor(26)
    setup(14)
try:
    GPIO.add_event_detect(14, GPIO.BOTH, callback = motion, bouncetime = 500)
    while True:
        time.sleep(1)

except :
    GPIO.cleanup()
