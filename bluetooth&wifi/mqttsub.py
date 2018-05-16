import paho.mqtt.client as mqtt
import LED

LED.Setup(4,"OUT")
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("LED")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload == b'turn on led':
            LED.TurnOnLED(4)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost",1883,60)
client.loop_forever()
