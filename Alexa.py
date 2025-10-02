import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception:
        print("Say that again please...")
        return ""   # safer than returning "None"
    return command.lower()

if __name__ == "__main__":
    wish()
    while True:
        command = take_command()

        if not command:   # skip empty commands
            continue

        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            query = command.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find that on Wikipedia.")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'make a note' in command or 'save note' in command:
            speak("What should I write?")
            note_content = take_command()
            if note_content:
                with open("note.txt", "a", encoding="utf-8") as f:
                    f.write(f"{datetime.datetime.now()}: {note_content}\n")
                speak("Note saved successfully.")
            else:
                speak("Sorry, I couldn't understand the note.")

        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

