import RPI.GPIO as GPIO, time, LED

def SetupPhotoresistor(GPIOpin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOpin, GPIO.IN)

def turnOnOffLED(GPIOpin, LDR_DO):
    if LDR_DO == 1:
        LED.TurnOnLED(GPIOpin)
    else:
        LED.TurnOffLED(GPIOpin)

if __name__ == "__main__":
    SetupPhotoresistor(2)
    LED.Setup(13, "OUT")
    while True:
        turnOnOffLED(26, GPIO.input(2))
        print(GPIO.input(2))
        time.sleep(1)
