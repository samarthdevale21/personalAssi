import pyttsx3  #pyttsx3 convert text in speech
import speech_recognition as sr
import datetime
import wikipedia
import pyaudio
import webbrowser

engine=pyttsx3.init('sapi5') 
voices=engine.getProperty('voices') 

engine.setProperty('voice',voices[0].id)

def speak(audio): 

    engine.say(audio)
    engine.runAndWait() 
def  Wishme(): 
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    
    else:
        speak("good evening")  

    speak("I am Sam please tell me how may i help you")

def sptext(): 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='en-in')
        data=r.recognize_google(audio)
        print(f"User said:{query}")
    except Exception as e:
            print("Please say again...")
            return "None"
    return query

if __name__=="__main__":
    Wishme()
    while True:
        query=sptext().lower()

        if 'wikipedia' in query:
            speak("search wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open Google' in query:
            webbrowser.open("open Google.com")

        elif 'the time is 'in query:
            strTime=datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'quit sam'in query:
            quit()
    
