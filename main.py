import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            return ""

def set_alarm(time):
    speak(f"Alarm set for {time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == time:
            speak("Wake up!")
            break

def add_task(task, due_date):
    tasks.append({"task": task, "due_date": due_date})
    speak(f"Task added: {task} due on {due_date}")

def set_reminder(time):
    speak(f"Reminder set for {time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == time:
            speak("Reminder!")
            break

tasks = []

speak("How can I help you?")
while True:
    command = listen().lower()
    if "set alarm" in command:
        time = command.split("set alarm for ")[1]
        set_alarm(time)
    elif "add task" in command:
        task = command.split("add task ")[1].split(" due on ")[0]
        due_date = command.split(" due on ")[1]
        add_task(task, due_date)
    elif "set reminder" in command:
        time = command.split("set reminder for ")[1]
        set_reminder(time)
    elif "quit" in command:
        speak("Goodbye!")
        break
