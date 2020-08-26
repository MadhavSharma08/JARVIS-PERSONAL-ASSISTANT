import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING")

    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON")

    else:
        speak("GOOD EVENING")

    speak("I AM JARVIS MASTER MADHAV . PLEASE TELL HOW MAY I HELP YOU?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("RECOGNIZING...")
        query = r.recognize_google(audio, language='en-in')
        print(f"USER SAID: {query}\n")

    except Exception as e:
        print(e)
        print("SAY THAT AGAIN PLEASE...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('factydude0866@gmail.com', 'factydude')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().upper()


        if 'wikipedia' in query:
            speak('SEARCHING WIKIPEDIA...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("ACCORDING TO WIKIPEDIA")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIR, THE TIME IS {strTime}")

        elif 'email to madhav' in query:
            try:
                speak("WHAT SHOULD I SAY?")
                content = takeCommand()
                to = "factydude0866@gmail.com"
                sendEmail(to, content)
                speak("EMAIL HAS BEEN SENT!!")
            except Exception as e:
                print(e)
                speak("SORRY MY MASTER MADHAV . I AM NOT ABLE TO SEND THIS EMAIL")
                