import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import re
import JarvisAI

obj = JarvisAI.JarvisAssistant()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Siri' in command:
                command = command.replace('Siri', '')
    except:
        pass
    return command


def run_siri():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif re.search('launch', command):
        dict_app = {
            'premiere Pro': 'C:\Program Files\Adobe\Adobe Premiere Pro 2020\Adobe Premiere Pro.exe',
            'origin': 'D:\Origin\Origin.exe',
            'browser': 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
            'discord': r'C:\Users\praba\AppData\Local\Discord\app-0.0.309\Discord.exe',
            'Dota 2': 'D:\Steam\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe',
        }
        app = command.split(' ', 1)[1]
        path = dict_app.get(app)
        if path is None:
            talk('Application path not found')
            print('Application path not found')
        else:
            talk('Launching: ' + app)
            obj.launch_any_app(path_of_app=path)


run_siri()