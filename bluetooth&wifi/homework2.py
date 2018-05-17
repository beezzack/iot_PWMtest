import socket
import RPi.GPIO as GPIO
import LED
import sys

bind_ip = '192.168.1.11'
bind_port = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = (bind_ip,bind_port)
print('connect to {} port {}'.format(*server_address))
client.connect(server_address)

LED.Setup(14, 'OUT')
try:
    print('Accepted connection')
    while True:
        data = client.recv(1024)
        print(data)
        if data == b'ture on led':
            LED.TurnOnLED(14)

except KeyboardInterrupt:
    client.close()
    GPIO.cleanup()

finally:
    server.close()
    GPIO.cleanup()
