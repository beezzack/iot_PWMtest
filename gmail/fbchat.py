import os,sys
from flask import Flask, request
import json
import requests
sys.path.append("../")
import LED
app = Flask(__name__)

ACCESS_TOKEN = "EAAClXHJ0bQkBAG8JrgjTvfiEiWBLciUdPPZBbak6pUTZB7eZAJ6HYtwgYYoBRTP9hxYIunbAKXtiQRPdZBjZC0xu7IDJu3ZA9ZA2ZBowh1RLzE7wFAQmZANMP47dQlt5zEQxPU2nquUeZCZA9DjZC5Pi43i1ZBFtXOYa67GArkoXtVAAyyQZDZD"

@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "Educational_Robots_and_Iots" :
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello woeld", 200

@app.route("/", methods=['POST'])
def webhook():
    data = request.get_json()

    if data["object"] == "page":
        for entry in data["entry"]:
            for msg_event in entry["messaging"]:
                sender_id = msg_event["sender"]["id"]

                if msg_event.get("message"):
                    message_text = msg_event["message"]["text"]
                    print(message_text)
                    if message_text == "turn on led":
                        LED.Setup(2,"OUT")
                        LED.TurnOnLED(2)
                        send_msg("", "Hi there")
                    else:
                        LED.Setup(2,"OUT")
                        LED.TurnOffLED(2)

                    print(message_text)
    log(data)
    return "ok",200

def send_msg(recipient_id, message_text):
    data = {
        "recipient": {"id": recipient_id},
        "message":{"text": message_text}
    }
    resp = requests.post("https://graph.facebook.com/v2.12/me/messages?access_token="+ ACCESS_TOKEN, json=data)
    print(resp.content)

def log(message):
    print(message)
    sys.stdout.flush()

if __name__=='__main__':
    app.run(debug=True, port=80)
