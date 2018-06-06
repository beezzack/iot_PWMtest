import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import LED

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER=7
GPIO_ECHO=12
GPIO_TEMP=4
GPIO_LED = 13

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
LED.Setup(GPIO_LED,"OUT")
sensor = Adafruit_DHT.DHT11
distance0 = 0
StopTime1 = 0
def send_trigger_pulse():
    GPIO.output(GPIO_TRIGGER ,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

def get_speed():
    humidity, temperature=Adafruit_DHT.read_retry(sensor, GPIO_TEMP)
    speed = 33100 + temperature * 60
    return speed

def get_velocity():
    global StopTime1, distance0 ,dist_error
    send_trigger_pulse()
    StopTime0 = StopTime1

    while GPIO.input(GPIO_ECHO)==0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        StopTime1 = time.time()

    TimeElapsed = StopTime1 - StartTime
    speed = get_speed()
    distance1 = TimeElapsed * speed * 0.5

    if distance1 < 2 or distance1 > 400 :
        dist_error = True
    else:
        dist_error = False

    velocity = (distance1-distance0)/(StopTime1 - StopTime0)
    distance0 = distance1

    return abs(velocity)

if __name__ == '__main__':
    try:
        global dist_error
        dist_error = False
        while True:
            velocity = get_velocity()
            if dist_error:
                print('Range Error: Range 2-400 cm')
            else:
                if velocity >= 50:
                    LED.TurnOnLED(GPIO_LED)
                else:
                    LED.TurnOffLED(GPIO_LED)
            print('velocity:', str(velocity)+ 'cm/sec')
            time.sleep(1)
    except KeyboardInterrupt:
            print("Measurement stopped by User")
            GPIO.cleanup()
