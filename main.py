import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    pass


if __name__ == "__main__":
    speak("Intializing Voice Assistant")
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = recognizer.listen(source, timeout= 2, phrase_time_limit=1) # Use the correct object here
                word = recognizer.recognize_google(audio) # And here
                if(word.lower() == "Wake up"):
                    speak("Yes")
                #Listen for command
                with sr.Microphone() as source:
                    print("Listening")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processcommand()



        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")