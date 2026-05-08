import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:

                # Better noise handling
                recognizer.adjust_for_ambient_noise(source, duration=1)

                print("Listening...")
                audio = recognizer.listen(source)

            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()

            print(f"User said: {command}")

            if "jarvis" in command:
                speak("Yes Ahmed, how can I help you?")

            elif "open google" in command:
                speak("Opening Google")
                webbrowser.open("https://google.com")

            elif "open youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://youtube.com")

            elif "exit" in command:
                speak("Goodbye Ahmed")
                break

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError:
            print("Internet error with speech recognition")

        except Exception as e:
            print("Error:", e)