import paha.mqtt.client as mqtt
import PhotoResistorDigitalSignal as PR
import RPi.GPIO as GPIOnum
PR.SetupPhotoresistor(2)

TopicServerIP = "localhost"
TopicServerPort = 1883
TopicName = "LED"

mqttc = mqtt.Client("pytion_pub")
mqttc.connect(TopicServerIP,TopicServerPort)

while True:
    PRstatus = GPIO.input(2)
    if PRstatus == 1:
        mqttc.publish(TopicName, "turn on led")
