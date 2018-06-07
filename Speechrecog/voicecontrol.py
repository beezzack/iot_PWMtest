import speech_recognition as sr
import LED

r=sr.Reconizer()
r.energy_threshold = 4000
LED.Setup(2,"OUT")

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        my_stt = r.recognize_google(audio, language = "en-US")

        if my_stt == "turn on LED":
            LED.TurnOnLED(2)
        elif my_stt == "turn off LED":
            LED.TurnOffLED(2)
        print(my_stt)

    except sr.UnknownValueError:
        print("Google Speech Reconition could not understand your audio")
    except sr.RequesError as e:
        print("Could not request results from Google speech Recognition service")
