import socket
import RPi.GPIO as GPIO
import LED

bind_ip = '192.168.2.185'
bind_port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))
print('Listening on %s:%d' %(bond_ip, bind_port))
LED.Setup(2, 'OUT')
try:
    client, addr = server.accept()
    print('Acepted connection from: %s:%d' %(addr[0], addr[1]))
    while True:
        data = client.recv(1024)
        if data == b'ture on led':
            LED.TurnOnLED(21)

except KeyboardInterrupt:
    client_socket.close()
    GPIO.cleanup()
