import RPi.GPIO as GPIO
import time
import LED

LED.Setup(2, "OUT")

try:
    while True:
        LED.TurnOnLED(2)
        time.sleep(1)
        LED.TurnOffLED(2)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
