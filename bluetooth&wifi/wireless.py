import socket
import RPi.GPIO as GPIO
import LED

bind_ip = '192.168.43.221'
bind_port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))
server.listen(5)
print('Listening on %s:%d' %(bind_ip, bind_port))
LED.Setup(2, 'OUT')
try:
    client, addr = server.accept()
    print('Accepted connection from: %s:%d' %(addr[0], addr[1]))
    while True:
        data = client.recv(1024)
        print(data)
        if data == b'ture on led':
            LED.TurnOnLED(21)

except KeyboardInterrupt:
    server.close()
    GPIO.cleanup()

finally:
    server.close()
    GPIO.cleanup()
