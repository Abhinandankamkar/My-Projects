import speech_recognition as sr # pyright: ignore[reportMissingImports]

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    
    audio = r.listen(source)
    
try:
    text = r.recognize_google(audio)
    print("You said: ",text)
    
except sr.UnknownValueError:
    print("Couldn't understant audio.")
    
except sr.RequestError:
    print("Error happend with service provider.")