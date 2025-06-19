import pyttsx3

text_engine = pyttsx3.init()

# text=input("Enter the text you want to convert to speech: ")

text_engine.say("Hello, this is a text-to-speech conversion example using Python.")
text_engine.runAndWait()