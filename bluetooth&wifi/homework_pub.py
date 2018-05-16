import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

TopicServerIP = "192.168.1.30"
TopicServerPort = 1883
TopicName = "PIR"

mqttc = mqtt.Client("homework_pub")
mqttc.connect(TopicServerIP,TopicServerPort)

def setup(GPIOnum):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOnum, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def motion(GPIOnum):
    mqttc.publish(TopicName, "milktea for sale")

if __name__ == "__main__":
    setup(14)
try:
    GPIO.add_event_detect(14, GPIO.BOTH, callback = motion, bouncetime = 500)
    while True:
        time.sleep(1)

except :
    GPIO.cleanup()
