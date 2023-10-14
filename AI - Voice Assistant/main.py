import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Didn't hear that. Please try again")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    if "titan" in sptext().lower():
        while True:
            data1 = sptext().lower()

            if "your name" in data1:
                name = "my name is Titan"
                speechtx(name)

            elif "hi" in data1:
                q1 = "Hi, How may I help you"
                speechtx(q1)

            elif "hey titan" in data1:
                q1 = "Hi, How may I help you"
                speechtx(q1)

            elif "how are you" in data1:
                howareyou = "I'm fine. What about you?"
                speechtx(howareyou) 

            elif "old are you" in data1:
                age = "I'm created on 7th January 2023 by GHOST"
                speechtx(age)

            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
                o1 = "Opening YouTube."
                speechtx(o1)

            elif "harvard introduction to computer science" in data1:
                webbrowser.open("https://www.edx.org/course/introduction-computer-science-harvardx-cs50x?index=product&queryID=b059b13731b5ef076171a75e8317a31b&position=1&eaid=0&v=1&linked_from=autocomplete&c=autocomplete")
                o2 = "Opening EDX CS50's Introduction to Computer Science."
                speechtx(o2)

            elif "browser" in data1:
                webbrowser.open("https://www.google.com/")
                o3 = "Opening Google Browser."
                speechtx(o3)

            elif "weather" in data1:
                webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=weather")
                o4 = "Opening Weather Updates, Kindly review."
                speechtx(o4)

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="all")
                print(joke_1)
                speechtx(joke_1)

            elif "play song" in data1:
                add = "path"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[0]))

            elif  "exit" in data1:
                terminate = "Termination Successful, thankyou for using"
                print("This AI is created by GHOST for EDX CS50 2023. Thank you for using.")
                speechtx(terminate)
                break

            #time.sleep(5)

    else:
        o5 = "Sorry, I didn't understand. Please try again"
        speechtx(o5)
        print("Command not found.")