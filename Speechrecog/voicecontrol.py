import speech_recognition as sr
import LED

r=sr.Recognizer()
r.energy_threshold = 4000
LED.Setup(2,"OUT")

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        my_stt = r.recognize_google(audio, language = "zh-tw")

        if my_stt == "打開":
            LED.TurnOnLED(2)
        elif my_stt == "關掉":
            LED.TurnOffLED(2)
        print(my_stt)

    except sr.UnknownValueError:
        print("Google Speech Reconition could not understand your audio")
    except sr.RequesError as e:
        print("Could not request results from Google speech Recognition service")
