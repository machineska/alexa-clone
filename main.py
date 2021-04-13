import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
listener.energy_threshold = 700  # setting usb mic for VIVIO HD
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#  engine.setProperty('voice', voices[17].id)
engine.setProperty('voice', 'english+f4')


voice_rate = 190
engine.setProperty('rate', voice_rate)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = None
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source, duration = 1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print(e)
    return command


def check_command(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        try:       
            info = wikipedia.summary(person, 1)
        except wikipedia.exceptions.PageError as e:
            info = e
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')



def run_alexa():
    command = take_command()
    print(command)
    if command:
        check_command(command)


try:
    while True:
        run_alexa()
except KeyboardInterrupt:
    pass

