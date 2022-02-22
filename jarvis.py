import pyttsx3

engine =pyttsx3.init("sapi5")
voices=engine.getproperty("voices")
print(voices[0])
engine.setProperty('voice' ,voices[0].id)


def speak(audio):
    pass