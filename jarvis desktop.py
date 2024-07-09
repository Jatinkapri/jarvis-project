import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os 
import smtplib
import pywhatkit 
from bs4 import BeautifulSoup
from time import sleep
import timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




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

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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

def open_netflix():
    netflix_url = "https://www.netflix.com/"
    webbrowser.open(netflix_url)

def open_amazon():
    amazon_url = "https://www.amazon.com/"
    webbrowser.open(amazon_url)


def open_whatsapp():
    whatsapp_url="https://web.whatsapp.com/"
    webbrowser.open(whatsapp_url)

def sendEmail(to,content):
    sender_email='joshivinayak931@gmail.com'
    sender_password='VINAYAK JOSHI 555' 

    message=MIMEMultipart()
    message['From']=sender_email
    message['To']=to
    message['Subject']= content 

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(sender_email,sender_password)
    server.sendmail("sender_email",to,content)
    server.close()
    
'''strTime = int(datetime.now().strftime("%H""%M"))
 
def sendMessage():
    speak("who do you want to message")
    a=int(input(''''''Ashish-1
                Yash-2
                vaibhav-3
                vinayak-4''''''
                ))
    if a == 1:
        speak("whats the message")
        message = str(input("enter the message-"))
        pywhatkit.sendwhatmsg("+918533847958",message,time_hour=strTime,time_min=strTime)
    elif a == 2:
        speak("whats the message")
        message = str(input("enter the message-"))
        pywhatkit.sendwhatmsg("+919268319936",message,time_hour=strTime,time_min=strTime)
    elif a == 3:
        speak("whats the message")
        message = str(input("enter the message-"))
        pywhatkit.sendwhatmsg("+919410755878",message,time_hour=strTime,time_min=strTime)
    elif a == 4:
        speak("whats the message")
        message = str(input("enter the message-"))
        pywhatkit.sendwhatmsg("+919675841744",message,time_hour=strTime,time_min=strTime)'''


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
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
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is ",(strTime))
        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\Documents"
            os.startfile(codePath)
        elif 'open netflix' in query:
            open_netflix()
        elif 'open amazon' in query:
            open_amazon()
        elif 'open whatsapp' in query:
            open_whatsapp()
        elif 'send email' in query:
            try:
                speak("whom do you what to send email")
                to=str(input("enter reciver email id"))
                speak("what should i send")
                content=str(input("enter the content to send"))
                sendEmail(to,content)
                speak("email sent successfully")       
            except Exception as e:
                print(e)
   