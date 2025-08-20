import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c = c.lower()
    if "youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    else:
        speak("Sorry, I can't do that yet.")

if __name__ == "__main__":
    speak("Initializing Voice Assistant")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio).lower()

            if word == "hello":   # wake word
                speak("Yes, I am listening")
                with sr.Microphone() as source:
                    print("Assistant Listening...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
