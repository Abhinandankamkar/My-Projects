import pyttsx3 # type: ignore

engine = pyttsx3.init()

text = "Hello! this is the first line of my text."

engine.say(text)

engine.runAndWait()