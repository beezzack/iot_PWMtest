import os,sys
from flask import Flask, request
import json
import requests
sys.path.append("../")
import LED
import RPi.GPIO as GPIO
import time
import multiprocessing as mp
app = Flask(__name__)
check = 0
ACCESS_TOKEN = "EAAClXHJ0bQkBAG8JrgjTvfiEiWBLciUdPPZBbak6pUTZB7eZAJ6HYtwgYYoBRTP9hxYIunbAKXtiQRPdZBjZC0xu7IDJu3ZA9ZA2ZBowh1RLzE7wFAQmZANMP47dQlt5zEQxPU2nquUeZCZA9DjZC5Pi43i1ZBFtXOYa67GArkoXtVAAyyQZDZD"
@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "Educational_Robots_and_Iots" :
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route("/", methods=['POST'])
def webhook():
    data = request.get_json()

    if data["object"] == "page":
        for entry in data["entry"]:
            for msg_event in entry["messaging"]:
                sender_id = msg_event["sender"]["id"]

                if msg_event.get("message"):
                    message_text = msg_event["message"]["text"]
                    #print(message_text)
                    if message_text == "turn off led":
                        LED.Setup(2,"OUT")
                        LED.TurnOffLED(2)
                        global check = 0
                        send_msg("1447614532010378", "turn off led")

                    #print(message_text)
    log(data)
    return "ok",200

def send_msg(recipient_id, message_text):
    data = {
        "recipient": {"id": recipient_id},
        "message":{"text": message_text}
    }
    resp = requests.post("https://graph.facebook.com/v2.12/me/messages?access_token="+ ACCESS_TOKEN, json=data)
    #print(resp.content)

def log(message):
    #print(message)
    sys.stdout.flush()
#--------------------------------------------------------------------------
def SetupPhotoresistor(GPIOpin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOpin,GPIO.IN)

def turnOnOffLED(GPIOpin, LDR_DO):
    if LDR_DO == 1:
        print("Dark")
        LED.TurnOnLED(GPIOpin)
    else:
        print("light")
        LED.TurnOffLED(GPIOpin)

def setup(GPIOnum):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOnum, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
counter = 0

def motion(GPIOnum):
    global counter,check
    if GPIO.input(GPIOnum):
        counter += 1
        if check = 0:
            turnOnOffLED(2,GPIO.input(26))
            print("Motion detected{0}".format(counter))
            send_msg("1447614532010378", "led is on")
            check = 1
        else:
            print("Motion detected{0} but is already light up".format(counter))
    else:
        print("Motion not detected")

def app_run():
    app.run(debug=True, port=80)


if __name__=='__main__':
    p1 = mp.Process(target=app_run)
    p1.start()
    LED.Setup(2,"OUT")
    SetupPhotoresistor(26)
    setup(14)
    try:
        GPIO.add_event_detect(14, GPIO.BOTH, callback = motion, bouncetime = 2000)
        while True:
            time.sleep(1)
    except :
        GPIO.cleanup()
    p1.join()
