import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak():
    engine.say("Hello Dear")
    engine.runAndWait()
    speak()