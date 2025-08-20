import speech_recognition as sr
import webbrowser
import pyttsx3
import music_lib
import requests

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()
key = "--"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    
    if "youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_lib.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={key}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
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
