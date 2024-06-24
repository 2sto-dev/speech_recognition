import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def SpeakText(command):
    engine.say(command)
    engine.runAndWait()
def ListenToSpeech():
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                print("Recognizing...")
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said: " + text)
            return text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred. Please try again.")

def main():
    while True:
        print("Speak something...")
        user_input = ListenToSpeech()
        SpeakText("You said: " + user_input)
if __name__ == "__main__":
    main()
