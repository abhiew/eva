                   
                        
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui #pip install pyautogui
import time

from pynput.keyboard import Key, Controller as K
from pynput.mouse import Button, Controller as M


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am EVA Abhi. Please tell me how may I help you")       

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def writer(word):
   
    time.sleep(2)
    M().position = (900,400)
    M().click(Button.left, 1)
    time.sleep(3)
    K().type(word)

def writer1(word):
    
    time.sleep(3)
    K().type(word)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
      query = takeCommand().lower()
      if 'EVA' in query:
          
          if 'type' in query:
            speak("What should I Type?")
            word = takeCommand()
            writer(word)
          
          elif 'message' in query:

              speak("What should I message?")
              msg = takeCommand()
              writer1(msg)
              pyautogui.press('enter')
           
          elif 'whatsapp' in query:
              os.system('whatsapp')  
          
          elif 'notepad' in query:
              os.system('notepad')

          elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
           
          elif 'open youtube' in query:
            webbrowser.open("youtube.com")

          elif 'open google' in query:
            webbrowser.open("google.com")
            speak("What should I Type?")
            search = takeCommand()
            writer1(search)


          elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

          elif 'play music' in query:
             music_dir = 'C:\\Users\\ASUS\\Videos\\RealPlayer Downloads'
             songs = os.listdir(music_dir)
             print(songs)    
             os.startfile(os.path.join(music_dir, songs[0]))

          elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
             speak(f"Sir, the time is {strTime}")

          elif 'open code' in query:
             codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)

          elif 'email to Pj' in query:
             try:
                speak("What should I say?")
                content = takeCommand()
                to = "abhiew.20@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
             except Exception as e:
                print(e)
                speak("Sorry my friend Abhi . I am not able to send this email")    
                  
      else:
              print('NOt for EVA')   
