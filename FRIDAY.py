import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

#https://www.youtube.com/watch?v=HWUsravMGLI&t=2925s&ab_channel=CodeXplore
FRIDAY = pyttsx3.init()
voice = FRIDAY.getProperty('voices')
FRIDAY.setProperty('voice',voice[1].id)

def speak(audio):
    print("FRIDAY : " + audio)
    FRIDAY.say(audio)
    FRIDAY.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p") #%I : số giờ, %M : số phút, %p : AM hoặc PM
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >=0 and hour <=12:
        speak("Good Morning Sir!")
    elif hour > 12 and hour <= 18:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")      
    speak("How can I help you?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print("Boss Duc : " + query)
    except sr.UnknownValueError:
        print("Please repeat or type your command")
        query = str(input("What is your idea? : "))
    return query


if __name__ == "__main__":
    query = command().lower()
    if "hey friday" in query:
        welcome()
        while True:
            query = command().lower()
            if "google" in query:
                speak("What do you want me to search Boss?")
                search = command().lower()
                url = f"https://www.google.com/search?q={search}"
                wb.get().open(url)
                speak(f"With this keyword {search}. I founnd  this on")
            elif "youtube" in query:
                speak("What do you want me to search Boss?")
                search = command().lower()
                url = f"https://www.youtube.com/search?q={search}"
                wb.get().open(url)
                speak(f"With this keyword {search}. I founnd  this on")
            elif "open movie" in query:
                speak("Opening your movie")
                strange= r"D:Phim\Doctor Strange In The Multiverse Of Madness\DoctorStrange.mp4"
                os.startfile(strange)
            elif "time" in query:
                time()
            elif "close" in query:
                speak("Have a good day. Goodbye sir")
                quit()
