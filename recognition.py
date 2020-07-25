import speech_recognition as sr
import time, datetime

timeout = time.time() + 60 * 20   # 10 minutes from now

#obtain audio from the microphone
r = sr.Recognizer()
i = 1
while time.time() < timeout:
    with sr.Microphone() as source:
        # print("Please wait. Calibrating microphone...")
        #listen for n seconds and create the ambient noise energy level
        # r.adjust_for_ambient_noise(source, duration = 1)
        print(f"sentence {i}...")
        audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            print("I thinks you said:")
            print(r.recognize_google(audio, language = "zh-TW"))
            i = i + 1
        except sr.UnknownValueError:
            print("I could not understand audio")
        except sr.RequestError as e:
            print("No response from Google Speech Recognition service: {0}".format(e))
