import RPi.GPIO as GPIO
import time
import LED

LED.Setup(2, "OUT")
LED.Setup(3, "OUT")

try:
    while True:
        LED.TurnOnLED(2)
        LED.TurnOffLED(3)
        time.sleep(1)
        LED.TurnOffLED(2)
        LED.TurnOnLED(3)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
