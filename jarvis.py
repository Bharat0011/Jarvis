import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0])

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good Morning!')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('Sir, I am Jarvis how can i help you ?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.energy_threshold =3500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print('Say that again....')
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            mysongs = random.choice(songs)
            songs[0] = mysongs
            print("My Songs",mysongs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'open code' in query:
            vscode_path = "C:\\Users\\h\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscode_path)

        elif 'stop' in query:
            exit()