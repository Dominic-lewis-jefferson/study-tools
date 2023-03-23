import speech_recognition as spr
import json

# Initializes the recogognition 
r = spr.Recognizer()

# Uses microphone as the audio source to record speaker
with spr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

# Uses Google's Speech Recognition service to recognize the audio to be able to turn it in to text 
try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except spr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except spr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

#Writes the transcribed text to a JSON file
data = {'text': text}
with open('output.json', 'w') as outfile:
    json.dump(data, outfile)

print("Output written to output.json")