import subprocess
import sys
import os
import datetime

def install_and_update_packages(packages):
    """Updates pip and installs the given list of packages."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ['SpeechRecognition', 'pyttsx3', 'pyaudio']


try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nI am now updating and installing libraries, to Speak and recive your voice commands.")
    import speech_recognition as sr
    import pyttsx3
    import pyaudio

except ImportError as e:
    print("\ninstalling...")
    datetime.sleep(2)
    install_and_update_packages(required_packages)
    # Try importing again after installation
    import speech_recognition as sr
    import pyttsx3
    import pyaudio
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nPackages installed successfully.")
    input("\nPress Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
r = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_commands():
    with sr.Microphone() as source:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nI am your voice assistance, Please ask me something.")
        print("\nListening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
            print()
            print(f"\nCommand received: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        return ""

def clock_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    return current_time

def clock_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")
    return current_date

def main():
    while True:
        command = listen_for_commands()
        if "hello" in command:
            print("\nHello There, I am MMU Whisper, your Smart Campus Voice Companion. You have successfully Tested the prototype, cant wait to show you the final results")
            speak("Hello There, I am MMU Whisper, your Smart Campus Voice Companion. You have successfully Tested the prototype, cant wait to show you the final results")

        elif "time" in command:
            current_time = clock_time()
            print("\nThe current time is "+ current_time)
            speak("The current time is " + current_time)
        
        elif "date" in command:
            current_date = clock_date()
            print("\nToday's date is " + current_date)
            speak("Today's date is "+ current_date)


        elif "exit" in command:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
