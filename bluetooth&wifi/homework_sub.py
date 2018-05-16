import paho.mqtt.client as mqtt
import socket
import RPi.GPIO as GPIO
bind_ip = '192.168.1.30'
bind_port = 8888

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("PIR")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    outputstring = msg.topic+" "+str(msg.payload)+"\n\t"
    byt = outputstring.encode()
    print(type(byt))
    conn_client.send(byt)



if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print('Listening on %s:%d' %(bind_ip, bind_port))
    try:
        conn_client, addr = server.accept()
        print('Accepted connection from: %s:%d' %(addr[0], addr[1]))
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("192.168.1.30",1883,60)
        client.loop_forever()
    except KeyboardInterrupt:
        server.close()
        GPIO.cleanup()

    finally:
        server.close()
        GPIO.cleanup()
