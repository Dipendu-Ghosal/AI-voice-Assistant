import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Intializing Voice Assistant")
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = recognizer.listen(source, timeout= 2) # Use the correct object here
                command = recognizer.recognize_google(audio) # And here
                print(command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")