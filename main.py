import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import webbrowser
import nltk

listener = sr.Recognizer()
player = pyttsx3.init()
voices = player.getProperty('voices')
player.setProperty('voice', voices[1].id)
volume =player.getProperty('volume')
player.setProperty('volume', 10.0)
rate = player.getProperty('rate')

player.setProperty('rate', rate - 25)



def listen():
    with sr.Microphone() as input_device:
        print("I am ready, Listening ....")
        voice_content = listener.listen(input_device)
        text_command = listener.recognize_google(voice_content)
        text_command = text_command.lower()
        print(text_command)

    return text_command;


def talk(text):
    player.say(text)
    print(text)
    player.runAndWait()


def run_voice_bot():
    while True:
        command = listen()
        if "what is your name" in command:
            command = command.replace("name", "")
            info = "not yet decided"
            talk(info)
            player.runAndWait()
        elif "how are you" in command:
            command = command.replace("how are you", "")
            info = "i am fine ,thank you"
            talk(info)
            player.runAndWait()
        elif "hello" in command:
            command = command.replace("hello", "")
            info = "heyyy! how can i help you"
            talk(info)
            player.runAndWait()
        elif "hi" in command:
            command = command.replace("hi", "")
            info = "hey there! how can i help you"
            talk(info)
            player.runAndWait()
        elif "what is your name" in command:
            command = command.replace("name", "")
            info = "voice bot"
            talk(info)
            player.runAndWait()
        elif "who made you" in command:
            command = command.replace("who made you", "")
            info = "haha,the people in front of you "
            talk(info)
            player.runAndWait()
        elif "who" in command:
            command = command.replace("who", "")
            info = wikipedia.summary(command, 5)
            talk(info)
            player.runAndWait()
        elif "what" in command:
            command = command.replace("what", "")
            info = wikipedia.summary(command, 5)
            talk(info)
            player.runAndWait()
            player.runAndWait()
        elif "where" in command:
            command = command.replace("where", "")
            info = wikipedia.summary(command, 5)
            talk(info)
            player.runAndWait()
        elif "how" in command:
            command = command.replace("how", "")
            info = wikipedia.summary(command, 5)
            talk(info)
            player.runAndWait()
        elif "play" in command:
            command = command.replace("play", "")
            pywhatkit.playonyt(command)
            player.runAndWait()
        elif "open youtube" in command:
            command = command.replace("open you tube", "")
            webbrowser.open('www.youtube.com')
            player.runAndWait()
        elif "open browser" in command:
            command = command.replace("open browser", "")
            webbrowser.open('www.google.com')
            player.runAndWait()


        elif "thank you" in command:
            command = command.replace("thank you", "")
            info = "You're welcome! Is there anything else I can help with?"
            talk(info)
            player.runAndWait()
        elif "bye" in command:
            
            command = command.replace("bye", "")
            info = "good gye! take care "
            talk(info)


        else:
            talk("Sorry, I am unable to find what you looking for")
run_voice_bot()