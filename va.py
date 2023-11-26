from email.mime import image
import pyttsx3
import speech_recognition as sr
import datetime,sys
import os
from googletrans import Translator
import time
import pyautogui 
import webbrowser
import wikipedia,pywhatkit,pyjokes
import smtplib
from turtle import *
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
from email.message import EmailMessage
import cv2
import requests
from playsound import playsound
#import pywhatkit
from tkinter import messagebox
from tkinter import *
import socket
import numpy as np
from tkinter import *
from tkinter import Tk
from pytube import YouTube
#from pygame import mixer
from pydictionary import Dictionary 
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from gui import Ui_MainWindow
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import keyboard
import instaloader
import PyPDF2 ,operator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
e=pyttsx3.init('sapi5')
voice=e.getProperty('voices')
#print(voice)
e.setProperty('voice',voice[1].id)
#messagebox.showinfo("note",'Update time of whatsapp, set time after 2 minute of current time')
#mixer.init()



def speak (audiovoice):
    #e.say('hello')
    print(audiovoice)
    e.say(audiovoice)
    e.runAndWait()


    
def dor():
    
    def ankur(x, y):
        penup()
        goto(x, y)
        pendown()


    def aankha():
        fillcolor("#ffffff")
        begin_fill()

        tracer(False)
        a = 2.5
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                lt(3)
                fd(a)
            else:
                a += 0.05
                lt(3)
                fd(a)
        tracer(True)
        end_fill()


    def daari():
        ankur(-32, 135)
        seth(165)
        fd(60)

        ankur(-32, 125)
        seth(180)
        fd(60)

        ankur(-32, 115)
        seth(193)
        fd(60)

        ankur(37, 135)
        seth(15)
        fd(60)

        ankur(37, 125)
        seth(0)
        fd(60)

        ankur(37, 115)
        seth(-13)
        fd(60)


    def mukh():
        ankur(5, 148)
        seth(270)
        fd(100)
        seth(0)
        circle(120, 50)
        seth(230)
        circle(-120, 100)


    def muflar():
        fillcolor('#e70010')
        begin_fill()
        seth(0)
        fd(200)
        circle(-5, 90)
        fd(10)
        circle(-5, 90)
        fd(207)
        circle(-5, 90)
        fd(10)
        circle(-5, 90)
        end_fill()


    def nak():
        ankur(-10, 158)
        seth(315)
        fillcolor('#e70010')
        begin_fill()
        circle(20)
        end_fill()


    def black_aankha():
        seth(0)
        ankur(-20, 195)
        fillcolor('#000000')
        begin_fill()
        circle(13)
        end_fill()

        pensize(6)
        ankur(20, 205)
        seth(75)
        circle(-10, 150)
        pensize(3)

        ankur(-17, 200)
        seth(0)
        fillcolor('#ffffff')
        begin_fill()
        circle(5)
        end_fill()
        ankur(0, 0)


    def face():
        fd(183)
        lt(45)
        fillcolor('#ffffff')
        begin_fill()
        circle(120, 100)
        seth(180)
        # print(pos())
        fd(121)
        pendown()
        seth(215)
        circle(120, 100)
        end_fill()
        ankur(63.56, 218.24)
        seth(90)
        aankha()
        seth(180)
        penup()
        fd(60)
        pendown()
        seth(90)
        aankha()
        penup()
        seth(180)
        fd(64)


    def taauko():
        penup()
        circle(150, 40)
        pendown()
        fillcolor('#00a0de')
        begin_fill()
        circle(150, 280)
        end_fill()


    def Doraemon():
        taauko()

        muflar()

        face()

        nak()

        mukh()

        daari()

        ankur(0, 0)

        seth(0)
        penup()
        circle(150, 50)
        pendown()
        seth(30)
        fd(40)
        seth(70)
        circle(-30, 270)

        fillcolor('#00a0de')
        begin_fill()

        seth(230)
        fd(80)
        seth(90)
        circle(1000, 1)
        seth(-89)
        circle(-1000, 10)

        # print(pos())

        seth(180)
        fd(70)
        seth(90)
        circle(30, 180)
        seth(180)
        fd(70)

        # print(pos())
        seth(100)
        circle(-1000, 9)

        seth(-86)
        circle(1000, 2)
        seth(230)
        fd(40)

        # print(pos())

        circle(-30, 230)
        seth(45)
        fd(81)
        seth(0)
        fd(203)
        circle(5, 90)
        fd(10)
        circle(5, 90)
        fd(7)
        seth(40)
        circle(150, 10)
        seth(30)
        fd(40)
        end_fill()

        seth(70)
        fillcolor('#ffffff')
        begin_fill()
        circle(-30)
        end_fill()

        ankur(103.74, -182.59)
        seth(0)
        fillcolor('#ffffff')
        begin_fill()
        fd(15)
        circle(-15, 180)
        fd(90)
        circle(-15, 180)
        fd(10)
        end_fill()

        ankur(-96.26, -182.59)
        seth(180)
        fillcolor('#ffffff')
        begin_fill()
        fd(15)
        circle(15, 180)
        fd(90)
        circle(15, 180)
        fd(10)
        end_fill()

        ankur(-133.97, -91.81)
        seth(50)
        fillcolor('#ffffff')
        begin_fill()
        circle(30)
        end_fill()
        # Doraemon with Python Turtle

        ankur(-103.42, 15.09)
        seth(0)
        fd(38)
        seth(230)
        begin_fill()
        circle(90, 260)
        end_fill()

        ankur(5, -40)
        seth(0)
        fd(70)
        seth(-90)
        circle(-70, 180)
        seth(0)
        fd(70)

        ankur(-103.42, 15.09)
        fd(90)
        seth(70)
        fillcolor('#ffd200')
        # print(pos())
        begin_fill()
        circle(-20)
        end_fill()
        seth(170)
        fillcolor('#ffd200')
        begin_fill()
        circle(-2, 180)
        seth(10)
        circle(-100, 22)
        circle(-2, 180)
        seth(180 - 10)
        circle(100, 22)
        end_fill()
        goto(-13.42, 15.09)
        seth(250)
        circle(20, 110)
        seth(90)
        fd(15)
        dot(10)
        ankur(0, -150)

        black_aankha()


    if __name__ == '__main__':
        screensize(900, 650, "#f0f0f0")
        pensize(3)
        speed(9)
        Doraemon()
        ankur(100, -300)
        write('Doremon', font=("Bradley Hand ITC", 30, "bold"))
        speak('Done sir!')
        speak('press close button to close')
        mainloop()
        

    
def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()
def Tran():
        
        speak("Tell Me The Line!")
        line = TakeHindi()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        speak(Text)
def greet():
    hour=int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M %p")
    
    if hour>=0 and hour<12:
        speak(f'Good morning sir, its {tt}')
    elif hour>=12 and hour<18:
        speak(f'Good afternoon sir, its {tt}')
    elif hour>=18 and hour<21:
        speak(f'Good evening sir, its {tt}')
    else:
        speak(f'its {tt} at night')
    speak('I am your personal Assistant')
    speak("My name is sonia.")
    
def news():
    main_url= "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=d7550b9e56334a4aa6c68a66bcc11601"
    main_page=requests.get(main_url).json()
    art=main_page['articles']
    head=[]
    day=['first','second','third','fourth','fifth']
    for ar in art:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
def ne():
    ma='https://newsapi.org/v2/top-headlines?country=in&apiKey=d7550b9e56334a4aa6c68a66bcc11601'
    main_page=requests.get(ma).json()
    art=main_page['articles']
    head=[]
    day=['first','second','third','fourth','fifth']
    for ar in art:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


'''def sendEmail(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('vaidyadev39@gmail.com', 'iuwiogwurrigcreu')

    email = EmailMessage()
    email['From'] = 'vaidyadev39@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
email_list = {
        'dude': 'vaidyadev2@gmail.com',
        'friend': 'ramilajoshi1699@gmail.com',
        
    }
'''
'''app_id='QU5P33-URJ583K7RQ'
                def computational_intelligence(question):
                    try:
                        client = wolframalpha.Client(app_id)
                        answer = client.query(question)
                        answer = next(answer.results).text
                        print(answer)
                        return answer
                    except:
                        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
                        return None'''
#speak('my audio voice')
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        while True:
           #self.taskExecution()
        
            speak('recognizing the user')
            speak('press close button or escape key to recognise again till you recognize successfully')
            recog=cv2.face.LBPHFaceRecognizer_create()
            recog.read('trainer/trainer.yml')
            casp='haarcascade_frontalface_default.xml'
            facecas=cv2.CascadeClassifier(casp)
            font=cv2.FONT_HERSHEY_SIMPLEX
            id=2
            names=['','Dev']
            cam=cv2.VideoCapture(0)
            cam.set(3,640)
            cam.set(4,200)
            minW=0.1*cam.get(3)
            minH=0.1*cam.get(4)
            while True:
                ret,img=cam.read()
                convert_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=facecas.detectMultiScale(convert_image,scaleFactor=1.2,minNeighbors=5,
                                            minSize=(int(minW),int(minH)))
                for(x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                    id,accuracy=recog.predict(convert_image[y:y+h,x:x+w])
                    if(accuracy<100):
                        id=names[id]
                        accuracy="{0}%".format(round(100-accuracy))
                        speak('verification successful')
                        speak("you are a genuine user welcome sir")
                        speak("please say wakeup for waking me! or goodbye to quit. otherwise i will not accept any command")
                        per=self.takevoicecommand()
                        if'wake up' in per:
                            self.taskExecution()
                        elif "goodbye" in per:
                            speak("Thanks for using me today")
                            sys.exit()
                        
                    else:
                        id='unknown'
                        accuracy="{0}%".format(round(100-accuracy))
                        speak('user authentication fails')
                        break
                        
                    cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                    cv2.putText(img,str(accuracy),(x+5,y+h-5),font,1,(255,255,0),1)#instead of id put accuracy here
                cv2.imshow('camera',img)
                
                
                k=cv2.waitKey(10)& 0xff
                if k==27:
                    break
        # print("Thanks for using this programme,have a good day")
            cam.release()
            cv2.destroyAllWindows()

           
            
           
            

                
    

    
 


    def takevoicecommand(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshhold=1
            try:
                audio=r.listen(source,timeout=30,phrase_time_limit=10)
                print("Compiling your voice please wait")
                text=r.recognize_google(audio,language='en-in').lower()
                print(f"sir said: {text}")
            except Exception as e:
                speak('unable to recognize your voice')
                return"Dev"
            return text.lower()
    def dict(self):
        
        from AyDictionary import AyDictionary
        dictionary = AyDictionary()
        
        speak("Activated dictionary!")

        speak("Tell me a word!")
        word=self.takevoicecommand()
        if 'meaning' in word:
            word=word.replace("what is the",'')
            #word=word.replace("of")
            
            word=word.replace("meaning of",'')
            #d=word.get()
            result=dictionary.meaning(word)
    
            speak(f"The meaning of {word} are {result}")
        elif 'synonym' in word:
            word=word.replace("what is the",'')
            #word=word.replace("of")
            word=word.replace("synonym of",'')
            result=dictionary.synonym(word)
            speak(f"The synonyms of {word} are {result}")
        elif "antonym" in word:
            word=word.replace("what is the",'')
            #word=word.replace("of")
            word=word.replace("antonym of",'')
            result=dictionary.antonym(word)
            
            speak(f"The antonyms of {word} are {result}")
        speak("Exited dictionary!")

        

    def screenshot(self):
        speak("Ok sir , What Should I Name That File ?")
        path = self.takevoicecommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\BRT301T\\Pictures\\Screenshots\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\BRT301T\\Pictures\\Screenshots")
        speak("Here Is Your ScreenShot")
    def  YoutubeAuto(self):
        speak("What is Your Command ?")
        comm = self.takevoicecommand()
        if 'pause' in comm:
            keyboard.press('space bar')
        elif 'play' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        speak("Done Sir")
    def pdf(self):
        speak("Enter the path of PDF")
        d=input("Enter the path here:")
        book=open(d,'rb')
        r=PyPDF2.PdfReader(book)
        no_of_pages= len(r.pages)
        print(f'{no_of_pages} pages')
        speak(f'PDF have {no_of_pages} pages')
        speak("Enter number of pages which you want i can read")
        pg=int(input("please enter NO. of pages to read:"))
        for i in range(0,pg):

            page= r.pages[i]
            text=page.extract_text()
            speak(text)
    def ChromeAuto(self):
        speak("What is Your Command ?")

        command = self.takevoicecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')
        speak('done sir')
        

    def askname(self):
        speak("who uses me?")
        speak('What is your name Sir ?')
        name= self.takevoicecommand()
        speak('Welcome ' f'{name} sir')
        speak('How can I help you sir ?')
    
    def taskExecution(self):
         pyautogui.press("escape")
         
         greet()
         self.askname()
         while True:
            self.work=self.takevoicecommand().lower()
            if 'how are you' in self.work or 'how r you' in self.work:
                speak('I am fine. Thank you')
                speak('How are you Sir ?')
            elif 'get your original voice' in self.work or 'get back your voice' in self.work:
                e=pyttsx3.init('sapi5')
                voice=e.getProperty('voices')
                #print(voice)
                e.setProperty('voice',voice[1].id)
                speak('I am getting back my orignal voice')
            


            elif 'what is your name' in self.work:
                speak("My name is sonia as i told earlier")
            elif 'who the heck is ' in self.work or 'what is this' in self.work or 'search about' in self.work:
                person = self.work.replace('who the heck is'or 'what is this' ,'')
                info =wikipedia.summary(person, 3)
                print(f'According to wikipedia: {info}')
                speak(f'According to wikipedia {info}')


            elif "open cmd" in self.work or 'open commandprompt' in self.work:
                speak("opening app")
                os.system("start cmd")
            elif 'change voice'in self.work or 'change the voice' in self.work:
                e=pyttsx3.init('sapi5')
                voice=e.getProperty('voices')
                rate=e.getProperty('rate')
                rate=e.setProperty(rate,75)
                #print(voice)
                e.setProperty('voice',voice[0].id)
                speak('hello your voice is changed')
            elif 'hi' in self.work or 'hello' in self.work:
                speak('hello it is good to see you')

            elif "alarm" in self.work:
                import time as r
                from pygame import mixer
                mixer.init()
                speak("Enter The Time in 24 hour format and separate with colon!")
                time = input("Enter The Time :")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        speak("Time To Wake Up Sir!")
                        mixer.music.load('c.mp3')
                        mixer.music.play()
                        r.sleep(10)
                        mixer.music.pause()
                        speak("Alarm Closed!")
                    elif now>time:
                            break
            
            
                        
            elif "shutdown" in self.work:
                  speak("shutting down system in 5 seconds")
                  os.system("shutdown /s /t 5")
            elif "restart" in self.work:
                os.system("shutdown /r /t 5")
                speak("restarting system in 5 seconds")
            elif 'sleep the system ' in self.work:
                speak('your system will be sleep ')
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif 'launch' in self.work:
                speak("Ok Sir , Launching.....")
                speak("tell website name")
                
                web1 = self.takevoicecommand()
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                speak("Launched!")
            elif 'website' in self.work:
                speak("Enter website name")
                web3=input("Enter the name:")
                web4 = 'https://www.' + web3 + '.com'
                webbrowser.open(web4)
                speak("Launched!")
                '''
            elif "alarm" in self.work:
                speak("sir tell me time to set alarm")
                speak("give command like, set alarm to 5:30 am")
                tt=self.takevoicecommand()
                tt=tt.replace("set alarm to ","")
                tt=tt.replace(".","")
                tt=tt.upper()
                import alarm
                alarm.alarm(tt)

            '''
            elif 'how many voice in my system' in self.work or 'how many voices i have' in self.work:
                e=pyttsx3.init('sapi5')
                voice=e.getProperty('voices')
                speak('This many voices you have')
                print(voice)
            elif "auto youtube" in self.work:
               speak('your youtube is now in auto mode')
               self.YoutubeAuto()
            elif "auto chrome" in self.work:
               speak('your chrome is now in auto mode')
               self.ChromeAuto()
            elif 'where i am' in self.work or 'where we are' in self.work or 'tell my location' in self.work:
                try:

                    speak('wait sir, let me check')
                    ip=requests.get('https://api.ipify.org').text
                    print(ip)
                    #49.34.38.162
                    #ip='192.168.16.177'
                   
                    url='https://get.geojs.io/v1/ip/geo/'+ip+'.json'
                    geo_r=requests.get(url)
                    geo_data=geo_r.json()
                    print(geo_data)
                    city=geo_data['city']
                    state=geo_data['region']
                    country=geo_data['country']
                    speak(f'sir i am not sure but i think we are in {city} city of {state} state of {country} country')
                except Exception as e:
                    speak('sorry sir!i am not able to track your location')
                    print(e)
            elif 'youtube search' in self.work:
                speak("OK sir , This Is What I found For Your Search!")
                #self.work = self.work.replace("jarvis","")
                q = self.work.replace("youtube search","")
                web = 'https://www.youtube.com/results?search_query=' + q
                webbrowser.open(web)
                speak("Done Sir!")

            elif 'draw' in self.work:
                speak('what you want to draw?')
                speak('I can draw doraemon and radha-krishna sketches for you')
                speak("press 1 for radha krishna or 2 for doraemon")
                speak('I can only draw for one time during session')
                speak('Enter your choice')
                dr=input('Enter your choice here:')
                if '1' in dr:
                    
                    import turtle
                    

                    #keeping the background color dark blue
                    turtle.bgcolor('#ffc233')

                    #Defining title of program
                    turtle.title("Radhe Krishna")

                    #Creating turtle screen
                    screen= turtle.Screen()
                    #Defining height and width of screen
                    screen.setup(650,580)

                    t1 = turtle.Turtle()

                    #keeping the fasted speed for now, you can keep the speed as needed
                    #'fastest' : 0
                    #'fast' : 10
                    #'normal' : 6
                    #'slow' : 3
                    #'slowest' : 1

                    t1.speed(4)

                    #Let's move down and go the position from where we will start to draw
                    t1.right(90)
                    t1.pu()
                    t1.forward(180)
                    t1.left(90)
                    #Now, the turtle is pointing positive x-axis

                    #Let's keep the pen down and start to draw the base
                    t1.pd()
                    #Here we have dipped our turtle brush in a shade of blue color
                    t1.fillcolor("#ff99d1")
                    t1.begin_fill()
                    t1.forward(400)
                    t1.right(90)
                    t1.forward(100)
                    t1.right(90)
                    t1.forward(800)
                    t1.right(90)
                    t1.forward(100)
                    t1.right(90)
                    t1.forward(400)
                    t1.end_fill()
                    #Now, we have drawn the base which is rectangular in shape
                    #end_fill will fill blue color (selected above), in the shape formed by turtle

                    #Now, we will start to draw moon,I have selected a very light shade of blue to color moon
                    t1.fillcolor("#CDEEF1")
                    t1.begin_fill()
                    t1.forward(160)
                    t1.left(40)
                    #this method will draw the moon's border  
                    t1.circle(250,280)
                    t1.left(40)
                    t1.forward(160)
                    t1.end_fill()
                    #Now, we have drawn the moon as well as filled color in it

                    #Now, we will start drawing Radha Krishna
                    #We will draw Radha on our right side and Krishna on left side
                    #We will start with Radha
                    t1.fillcolor("#012427")
                    t1.begin_fill()
                    #We will start with the duppata
                    t1.forward(160)
                    t1.left(130)
                    t1.circle(-300,30)
                    t1.forward(95)
                    #This will draw the shoulder
                    t1.circle(50,40)
                    t1.right(40)
                    #This will draw the head
                    t1.forward(43)
                    t1.circle(80,25)
                    t1.circle(50,30)
                    t1.left(10)
                    t1.circle(35,28)
                    #Now, we have completed drawing Radha

                    #Now, let's draw krishna's turban
                    t1.right(160)
                    t1.circle(10,100)
                    t1.right(100)
                    t1.circle(10,80)
                    t1.forward(20)
                    t1.left(80)
                    t1.circle(100,15)
                    t1.right(90)
                    t1.forward(6)
                    t1.left(65)
                    t1.circle(60,55)

                    #Following code will draw Krishna's morpankh
                    t1.right(160)
                    t1.circle(20,100)
                    t1.forward(10)
                    t1.circle(-20,25)
                    t1.left(170)
                    t1.circle(-20,40)
                    t1.forward(10)
                    t1.circle(20,80)
                    #morpankh done

                    #We will continue to draw rest part of turban
                    t1.right(135)
                    t1.circle(60,15)
                    t1.left(70)
                    t1.forward(6)

                    t1.right(110)
                    t1.forward(9)

                    t1.left(80)
                    t1.circle(70,24)

                    t1.right(60)
                    t1.circle(65,30)
                    t1.circle(-5,110)

                    #Below lines of code will draw the right hand of Krishna
                    t1.circle(5,120)
                    t1.right(90)
                    t1.circle(5,60)
                    t1.forward(10)
                    t1.circle(10,5)
                    t1.right(80)
                    t1.forward(15)
                    t1.circle(-5,160)
                    #Now, we will draw the first open finger of right hand
                    t1.forward(6)
                    t1.circle(2,180)
                    t1.forward(6)
                    t1.circle(20,30)

                    #Below lines will draw fingers holding bansuri
                    t1.right(140)
                    t1.circle(3,150)
                    t1.right(110)
                    t1.circle(4,80)
                    t1.forward(2)
                    t1.right(100)

                    #Here, we will draw second open finger of krishna
                    t1.forward(6)
                    t1.right(60)
                    t1.forward(9)
                    t1.circle(2,180)
                    t1.forward(10)
                    t1.left(30)
                    t1.forward(15)

                    #We will now start to draw bansuri
                    t1.right(85)
                    t1.forward(40)
                    t1.right(60)
                    t1.circle(5,310)
                    t1.right(80)
                    t1.forward(3)
                    t1.right(90)

                    #dor on bansuri
                    t1.forward(42)
                    t1.right(30)
                    t1.forward(10)
                    t1.left(90)
                    t1.circle(20,60)
                    t1.left(95)
                    t1.forward(12)
                    t1.right(29)
                    t1.forward(42)

                    #We will draw the rest part of bansuri
                    t1.right(90)
                    t1.forward(34)
                    t1.right(85)

                    #left hand of Krishna
                    t1.forward(2)
                    t1.circle(60,25)

                    #Now, we will draw Krishna's duppata
                    t1.right(80)
                    t1.circle(10,40)
                    t1.forward(45)
                    t1.left(10)
                    t1.forward(130)

                    #Below lines will draw the plates of duppata
                    t1.left(90)
                    t1.forward(20)
                    t1.right(90)
                    t1.forward(10)
                    t1.left(90)
                    t1.forward(10)
                    t1.right(90)
                    t1.forward(5)
                    t1.left(90)
                    t1.forward(25)

                    #This will complete drawing duppata
                    t1.left(100)
                    t1.forward(120)

                    t1.right(175)
                    t1.circle(50,50)

                    #Now, we will tilt turtle towards required direction and draw Krishna's dhoti
                    t1.right(80)
                    t1.circle(110,15)
                    t1.forward(75)

                    #The turtle will now reach to the rectangular base we had drawn in the beginning
                    t1.left(97)
                    t1.forward(260)
                    t1.end_fill()
                    #At this point, we have completed drawing Radhe Krishna

                    t1.pu()
                    t1.right(90)
                    t1.forward(100)
                    t1.right(90)
                    t1.forward(420)

                    #Lets also write their holy name in our drawing 
                    t1.color("#00a606")
                    t1.write("Radhe Krishna....", font=("Script",45, "bold"))

                    t1.hideturtle()
                    speak('Done sir!')
                    speak('press close button to close')
                    turtle.done()
                    
                   


                    
                elif '2' in dr:
                    
                    dor()
                    
                    
                else:
                    speak('invalid choice!')



            elif 'google search' in self.work:
                
                try:
                    
                    import wikipedia as googleScrap
                    
                    que = self.work.replace("google search","")
                    que= que.replace("google","")
                    result = googleScrap.summary(que,2)
                    speak("OK sir , This Is What I found For Your Search!")
                    pywhatkit.search(que)
                    speak(result)
                    speak("Done Sir!")
                    
                    
                except Exception as e:
                        print(e)
                        speak("No Speakable Data Available!")
            elif 'insta profile' in self.work or 'instagram profile' in self.work:
                import time
                speak("please enter the user name correctly")
                name=input("Enter user name:")
                webbrowser.open(f'www.instagram.com/{name}')
                time.sleep(5)
                speak("sir would you like to download profile picture of this account speak yes for yes")
                co=self.takevoicecommand()
                if'yes'in co:
                    mod=instaloader.Instaloader()
                    mod.download_profile(name,profile_pic_only=True)
                    speak('I am done sir,profile pic is saved to your main folder')
                else:
                    pass
            elif'read pdf' in self.work:
               
               self.pdf()
            
            elif 'do some calculation' in self.work or 'can you calculate' in self.work or 'calculate' in self.work:
                try:

                    r=sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("What you want to calculate, give command like 3 plus 3 ")
                        print('Recognizing...')
                        r.adjust_for_ambient_noise(source)
                        audio=r.listen(source)
                        my_s=r.recognize_google(audio,language='en-in').lower()
                        print(my_s)
                   
                    def get(op):
                        return{
                            '+':operator.add,#plus
                            '-':operator.sub,#minus
                            'x':operator.mul,#multiplied by
                            '/' :operator.__truediv__,#divided
                            


                        }[op]
                    def eval_binaary_exp(op1,oper,op2):

                        op1,op2=float(op1),float(op2)
                        return get(oper)(op1,op2)
                    speak("Your result is")
                    speak(eval_binaary_exp(*(my_s.split())))
                except Exception as e:
                    print(e)
                    speak('i cannot understand plese speak again')
            #elif 'calculation' in self.work:
                #import wolframalpha
                
                #question = self.taskExecution()'''
                #answer = computational_intelligence(question)
                #speak(answer)
    

            elif 'open netbeans' in self.work:
                speak("opening app")
                path="C:\\Program Files\\NetBeans-18\\netbeans\\bin\\netbeans64.exe"
                os.startfile(path)

            elif 'close netbeans' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM netbeans64.exe")


            elif 'open pycharm' in self.work:
                speak("opening app")
                path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.3\\bin\\pycharm64.exe"
                os.startfile(path)

            elif 'close pycharm' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM pycharm64.exe")

            elif 'open sublime' in self.work:
                speak("opening app")
                path="C:\\Program Files\\Sublime Text\\sublime_text.exe"
                os.startfile(path)

            elif 'close sublime' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM sublime_text.exe")

            elif 'open eclipse' in self.work:
                speak("opening app")
                path="C:\\Users\\BRT301T\\java-2023-033\\eclipse\\eclipse.exe"
                os.startfile(path)
            elif'login my facebook' in self.work :

                import time
                def account_info():
                     with open('ac.txt','r') as f:
                            info=f.read().split()
                            email =info[0]
                            password=info[1]
                            return email,password
                email,password=account_info()
                #tweet=input("Enter your message:")
                option= Options()
                option.add_argument('--disable-notifications')

                option.add_argument('start-maximized')
                driver=webdriver.Chrome(options=option)
                driver.get("https://www.facebook.com")
                email_xpath='//*[@id="email"]'
                post='#mount_0_0_Pt > div > div:nth-child(1) > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x1qjc9v5.xozqiw3.x1q0g3np.x1t2pt76.x17upfok > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x1iyjqo2.xs83m0k.xeuugli.xl56j7k.x1qjc9v5.xozqiw3.x1q0g3np.x1iplk16.x1xfsgkm.xqmdsaz.x1mtsufr.x1w9j1nh > div > div > div > div.x78zum5.x1q0g3np.xl56j7k > div > div.x1yztbdb > div > div > div > div.x1cy8zhl.x78zum5.x1iyjqo2.xs83m0k.xh8yej3 > div > div.xi81zsa.x1lkfr7t.xkjl1po.x1mzt3pk.xh8yej3.x13faqbe'
                tw='#scrollview > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x1qjc9v5.xozqiw3.x1q0g3np.x1t2pt76.x17upfok > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x1iyjqo2.xs83m0k.xeuugli.xl56j7k.x1qjc9v5.xozqiw3.x1q0g3np.x1iplk16.x1xfsgkm.xqmdsaz.x1mtsufr.x1w9j1nh > div > div > div > div.x78zum5.x1q0g3np.xl56j7k > div > div.x1yztbdb > div > div > div > div.x1cy8zhl.x78zum5.x1iyjqo2.xs83m0k.xh8yej3 > div > div.xi81zsa.x1lkfr7t.xkjl1po.x1mzt3pk.xh8yej3.x13faqbe > span'
                t='//*[@id="mount_0_0_kJ"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div'
                time.sleep(5)
                driver.find_element("xpath",email_xpath).send_keys(email)
                time.sleep(5)
                driver.find_element("name","pass").send_keys(password)
                time.sleep(2)
                driver.find_element("name","login").click()
                time.sleep(20)
                speak('your account is logged in')










            elif 'close eclipse' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM eclipse.exe")

            elif 'open database' in self.work:
                speak("opening app")
                path="C:\\Program Files\\DB Browser for SQLite\\DB Browser for SQLite.exe"
                os.startfile(path)

            elif 'close database' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM DB Browser for SQLite.exe")

            elif 'open rstudio' in self.work:
                speak("opening app")
                path="C:\\Program Files\\RStudio\\rstudio.exe"
                os.startfile(path)

            elif 'close rstudio' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM rstudio.exe")

            elif 'brightness'in self.work:
                import screen_brightness_control as pct
                speak(f'your currnet brightness level is{pct.get_brightness()} percentage')
                speak('Enter the brightness level percentage to be set')
                level=input("Enter brightness level here:")
                pct.set_brightness(level)
                speak(f'your brightness level is set to{pct.get_brightness()} percentage')

            

           
            
            
                
                


            
                

           





                
            elif 'time' in self.work:
                time =datetime.datetime.now().strftime('%H:%M: %p')
                speak('Current time is ' +time)
                
            elif 'play' in self.work:
                song= self.work.replace('play', '')
                speak('playing' + song)
                pywhatkit.playonyt(song)

            
            elif 'start music' in self.work:
                speak("Enter your folder path")
                music_dir = ("Enter your folder path here:")
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'send whatsapp' in self.work:
                speak("to whom you send ? ")
                f=input('whom:')
                #f=self.takevoicecommand()
                m_list = {
                'dude': '+919023493913',
                'friend': '+919998847516',
                }
                fv=m_list[f]
                speak('what should i send ?')
                msg=input('message:')
                #msg=self.takevoicecommand()
                #speak("Tell me time!")
                #speak('Time in Hour')
                h=int (input('hour:'))
                #h=self.takevoicecommand()
                #speak('Time in Minute')
                m=int (input('miniute:'))
                #m=self.takevoicecommand()
                
                pywhatkit.sendwhatmsg(fv,msg,h,m)
                speak('message send')
                
            elif 'tell my ip' in self.work or 'tell my ip address' in self.work:
                hostname=socket.gethostname()
                IP=socket.gethostbyname(hostname)
                speak(f'Your Device name is:{hostname}')
                speak(f'your IP-Address is:{IP}')
            elif 'take screenshot' in self.work:
                self.screenshot()
            

                


                
            elif 'joke' in self.work:
                speak(pyjokes.get_joke())


            elif 'open word' in self.work:
                speak("opening app")
                path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(path)

                
            elif 'close word' in self.work or 'close it' in self.work :
                speak("closing app")
                os.system("TASKKILL /F /IM WINWORD.EXE")


                
            elif 'open wordpad'in self.work or 'close it'in self.work:
                speak("opening app")
                path="C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
                os.startfile(path)

           

            elif 'open camera' in self.work:
                import cv2
                cap=cv2.VideoCapture(0)
                speak("press q for quit")
                while True:
                    ret,im=cap.read()
                    cv2.imshow("webcam",im)
                    if cv2.waitKey(1)==ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        break

            
                        



                
            elif 'close wordpad' in self.work or 'close it' in self.work :
                speak("closing app")
                os.system("TASKKILL /F /IM wordpad.exe")

                
            elif 'open powerpoint' in self.work:
                speak("opening app")
                path="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(path)

                
            elif 'close powerpoint' in self.work or 'close it' in self.work :
                speak("closing app")
                os.system("TASKKILL /F /IM POWERPNT.EXE ")

                
            elif 'open excel' in self.work:
                speak("opening app")
                path="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(path)

                
            elif 'close excel' in self.work or 'close it' in self.work :
                speak("closing app")
                os.system("TASKKILL /F /IM EXCEL.EXE ")

                
            elif 'open tally' in self.work:
                speak("opening app")
                path="C:\\Program Files\\Tally\\Tally.ERP9\\tally.exe"
                os.startfile(path)

                
            elif 'close tally' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM tally.exe ")
            

            
            elif 'open kompozer' in self.work:
                speak("opening app")
                path="C:\\Program Files (x86)\\KompoZer\\kompozer.exe"
                os.startfile(path)

                
            elif 'close kompozer' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM kompozer.exe ")


                
            elif 'open java' in self.work:
                speak("opening app")
                path="C:\\Users\\BRT301T\\Desktop\\scantilla\\Sc523.exe"


                
            elif 'close java' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM Sc523.exe ")

                
            elif  'I am fine' in self.work or 'fine' in self.work or 'good' in self.work:
                speak('It is good to know that you are fine')

                
            elif 'thank you' in self.work or 'thanks' in self.work:
                speak('Welcome')

                
            elif  'i love you' in self.work or 'love you'in self.work or 'i love u' in self.work:
                speak('OH MY GOD THANK YOU')

                
            
            elif 'open chrome' in self.work:
                speak("opening app")
                path='C://Program Files//Google//Chrome//Application//chrome.exe'
                os.startfile(path)



                
            elif 'close chrome' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM chrome.exe")

           
            elif 'repeat my word' in self.work:
                speak("Speak Sir!")
                jj = self.takevoicecommand()
                speak(f"You Said : {jj}")
    


                
            elif 'open google' in self.work :
                speak("opening app")
                url="gogle.com"
                path='C://Program Files//Google//Chrome//Application//chrome.exe %s'
                webbrowser.get(path).open(url)


                
            elif 'close google' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM chrome.exe")
            elif 'tweet' in self.work:
                import time
                def account_info():
                    with open('account_info.txt','r') as f:
                        info=f.read().split()
                        email =info[0]
                        password=info[1]
                    return email,password
                email,password=account_info()
                speak("What should i tweet?")
                tweet=input("Enter your tweet:")
                option= Options()
                option.add_argument('start-maximized')
                driver=webdriver.Chrome(options=option)

                driver.get("https://twitter.com/i/flow/login")
                email_xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
                nex='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
                log='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'
                post='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
                pos='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
                p='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span'
                time.sleep(10)
                driver.find_element("xpath",email_xpath).send_keys(email)
                time.sleep(5)
                driver.find_element("xpath",nex).click()
                time.sleep(5)
                driver.find_element("name","password").send_keys(password)
                time.sleep(5)
                driver.find_element("xpath",log).click()
                time.sleep(5)
                driver.find_element("xpath",post).click()
                time.sleep(15)
                driver.find_element(By.CSS_SELECTOR,"#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1habvwh.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-rsyp9y.r-1pjcn9w.r-htvplk.r-1udh08x.r-1potc6q > div > div > div > div:nth-child(3) > div.css-1dbjc4n.r-14lw9ot.r-1pp923h.r-1moyyf3.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-18u37iz.r-184en5c > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div").send_keys(tweet)
                time.sleep(10)
                driver.find_element("xpath",p).click()
                time.sleep(20)
                speak('your message is successfuly tweet')

                
            elif 'open youtube' in self.work:
                speak("opening app")
                webbrowser.open('https://www.youtube.com')
                
                    



                
            elif 'close youtube' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM chrome.exe")


                
            elif 'open gmail' in self.work:
                speak("opening app")
                url="mail.google.com"
                path='C://Program Files//Google//Chrome//Application//chrome.exe %s'
                webbrowser.get(path).open(url)


            elif 'close gmail' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM chrome.exe")

            elif 'open chat ' in self.work:
                speak("opening app")
                url="chat.openai.com"
                path='C://Program Files//Google//Chrome//Application//chrome.exe %s'
                webbrowser.get(path).open(url)

            elif 'temperature'in self.work:
                speak("Tell Me The Name Of the Place ")
                searc=self.takevoicecommand()
                search=f'temperature in {searc}'
                url=f'https://www.google.com/search?q={search}'
                r=requests.get(url)
                data=BeautifulSoup(r.text,'html.parser')
                temp=data.find("div",class_="BNeawe").text
                speak(f'current temperature in {searc} is {temp}')
                speak("Do I Have To Tell You Another Place Temperature ?")
                next = self.takevoicecommand()

                if 'yes' in next:
                    speak("Tell Me The Name Of the Place ")
                    name = self.takevoicecommand()
                    search = f"temperature in {name}"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temperature = data.find("div",class_ = "BNeawe").text
                    speak(f"The Temperature in {name} is {temperature} ")

                else:
                    speak("no problem sir")

            elif'how much power left' in self.work or 'battery' in self.work:
                import psutil 
                def converttime(seconds):
                    minutes,seconds=divmod(seconds,60)
                    hours,minutes=divmod(minutes,60)
                    return"%d:%02d:%02d"%(hours,minutes,seconds)
                battery =psutil.sensors_battery()
                per=battery.percent
                time=converttime(battery.secsleft)
                speak(f'sir you have {per} percent battery')
                speak(f'battery will remain for {time} hour')
                if per>=75:
                    speak('you have enough power to continue work')
                elif per>40 and per <=75:
                    speak("you should connect our pc with charger")
                elif per>10 and per <=40:
                    speak('you donot have enough power to continue work')
                elif per<10:
                    speak("you must connect our pc with charger")
            elif 'internet speed' in self.work or 'speed' in self.work:
                try:
            
                    import speedtest
                    speed=speedtest.Speedtest()
                    down=speed.download()
                    down_mbs=round(down/(10**6),2)
                    up=speed.upload()
                    up_mbs=round(up/(10**6),2)
                    servername=[]
                    ping=speed.get_servers(servername)
                    ping1=speed.results.ping
                    speak(f'Your Download speed is {down_mbs} mb per second')
                    speak(f'Your Upload speed is {up_mbs} mb per second')
                    speak(f'Your ping or latency is {ping1} milliseconds')
                except:
                    speak("there is no internet connection")

            elif 'volume up' in self.work:
                pyautogui.press('volumeup')
                speak("i increased your volume level")
            elif 'volume down' in self.work:
                pyautogui.press('volumedown')
                speak("i decreased your volume level")
            elif 'volume mute' in self.work or 'mute' in self.work:
                pyautogui.press('volumemute')
                speak("i mute your speaker")
            #4ad273576b87a54786f7e8c1e426b679
            #+15404277232
            elif'message' in self.work:
                speak("to whom you send ? ")
                
                f=self.takevoicecommand()
                speak('what is your message?')
                msz=self.takevoicecommand()
                m_list = {
                'dude': '+919023493913',
                'friend': '+919998847516',
                
                }
                fv=m_list[f]
                from twilio.rest import Client

                account_sid = 'AC8b360569f323a7cd76e5c0e71fc803bd'
                auth_token = '4ad273576b87a54786f7e8c1e426b679'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                body=msz,
                from_='+15404277232',
                to=fv
                )

                print(message.sid)
                speak("message has been delievered")
            elif'call' in self.work:
                speak("to whom you call? ")
                
                f=self.takevoicecommand()
                
                m_list = {
                'dude': '+919023493913',
                'friend': '+919998847516',
                }
                fv=m_list[f]
                
                from twilio.rest import Client
               

                account_sid = 'AC8b360569f323a7cd76e5c0e71fc803bd'
                auth_token = '4ad273576b87a54786f7e8c1e426b679'
                client = Client(account_sid, auth_token)

                message = client.calls.create(
                twiml='<Response><Say>This is a testing call..</Say></Response>',
                from_='+15404277232',
                to=fv
                )

                print(message.sid)
                speak('your call is delivered')




            elif 'open phone camera' in self.work or 'open mobile camera' in self.work:
                speak('your camera is opening press q for exit')
                import urllib.request
                import cv2 
                import numpy as np
                import time
                speak("Enter the url of picture captured")
                URL=input('Enter your IP here:')
                #URL='http://192.168.26.186:8080/shot.jpg'
                while True:
                    img_arr=np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img=cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPwebcam',img)
                    q=cv2.waitKey(1)
                    if q==ord('q'):
                        break;
                cv2.destroyAllWindows()
        

            elif 'close chat ' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM chrome.exe")


            elif 'open stack ' in self.work:
                speak("opening app")
                url="stackoverflow.com"
                path='C://Program Files//Google//Chrome//Application//chrome.exe %s'
                webbrowser.get(path).open(url)

            elif 'close stack ' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM chrome.exe")

            elif 'hide all file' in self.work or 'visible folder' in self.work:
                speak("sir please tell me you want to hide this folder or make it visible to everyone")
                con=self.takevoicecommand()
                if 'hide' in con:
                    os.system('attrib +h /s /d')
                    speak("all the file in this folder are now hidden")
                elif 'visible' in con:
                    os.system('attrib -h /s /d')
                    speak("all the file in this folder are now visible to everyone")
                elif 'leave it'in con:
                    speak('Ok sir!')
                else:
                    pass

            elif 'remember that' in self.work or 'remember' in self.work:
                speak("what you want i can remember")
                rem=self.takevoicecommand()
                speak('you tell me to remind:'+rem)
                remember=open("data.txt",'w')
                remember.write(rem)
                remember.close()
            elif 'what do you remember' in self.work or 'tell me what inside your memory' in self.work:
                remeberr = open('data.txt','r')
                speak("You Tell Me That:" + remeberr.read())
            elif 'what can you do' in self.work:
                global ren
                import time
                ren =  open('jarvistodo.txt','r')
                speak("I can do following thing I have Following feature")
                speak("you have to give following command to access me")
                print(ren.read())
                time.sleep(10)
            



            

                    

                


                


                
        

                
            elif 'open app store' in self.work:
                speak("opening app")
                url="https://play.google.com"
                path='C://Program Files//Google//Chrome//Application//chrome.exe %s'
                webbrowser.get(path).open(url)

                
            elif 'close app store' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM chrome.exe")

                
            elif 'open meet' in self.work:
                speak("opening app")
                url="https://meet.google.com"
                path='C://Program Files//Google//Chrome//Application//chrome.exe %s'
                webbrowser.get(path).open(url)
            elif 'who made you' in self.work or 'who developed you' in self.work:
                speak('I was made by dev vaidya at 2023')
                
            elif 'close meet' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM chrome.exe")
            elif 'game' in self.work or 'play' in self .work:
                # build 2048 in python using pygame!!
                import pygame
                import random
                global score
                pygame.init()
                speak('This is 2048  like game, play and enjoy!')
                speak('your  high score will be recorded')
                # initial set up
                WIDTH = 400
                HEIGHT = 500
                screen = pygame.display.set_mode([WIDTH, HEIGHT])
                pygame.display.set_caption('2048')
                timer = pygame.time.Clock()
                fps = 60
                font = pygame.font.Font('freesansbold.ttf', 24)

                # 2048 game color library
                colors = {0: (204, 192, 179),
                        2: (238, 228, 218),
                        4: (237, 224, 200),
                        8: (242, 177, 121),
                        16: (245, 149, 99),
                        32: (246, 124, 95),
                        64: (246, 94, 59),
                        128: (237, 207, 114),
                        256: (237, 204, 97),
                        512: (237, 200, 80),
                        1024: (237, 197, 63),
                        2048: (237, 194, 46),
                        'light text': (249, 246, 242),
                        'dark text': (119, 110, 101),
                        'other': (0, 0, 0),
                        'bg': (187, 173, 160)}

                # game variables initialize
                board_values = [[0 for _ in range(4)] for _ in range(4)]
                game_over = False
                spawn_new = True
                init_count = 0
                direction = ''
                score = 0
                file = open('high_score', 'r')
                init_high = int(file.readline())
                file.close()
                high_score = init_high


                # draw game over and restart text
                def draw_over():
                    pygame.draw.rect(screen, 'black', [50, 50, 300, 100], 0, 10)
                    game_over_text1 = font.render('Game Over!', True, 'white')
                    game_over_text2 = font.render('Press Enter to Restart', True, 'white')
                    screen.blit(game_over_text1, (130, 65))
                    screen.blit(game_over_text2, (70, 105))


                # take your turn based on direction
                def take_turn(direc, board):
                    global score
                    merged = [[False for _ in range(4)] for _ in range(4)]
                    if direc == 'UP':
                        for i in range(4):
                            for j in range(4):
                                shift = 0
                                if i > 0:
                                    for q in range(i):
                                        if board[q][j] == 0:
                                            shift += 1
                                    if shift > 0:
                                        board[i - shift][j] = board[i][j]
                                        board[i][j] = 0
                                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift][j] \
                                            and not merged[i - shift - 1][j]:
                                        board[i - shift - 1][j] *= 2
                                        score += board[i - shift - 1][j]
                                        board[i - shift][j] = 0
                                        merged[i - shift - 1][j] = True

                    elif direc == 'DOWN':
                        for i in range(3):
                            for j in range(4):
                                shift = 0
                                for q in range(i + 1):
                                    if board[3 - q][j] == 0:
                                        shift += 1
                                if shift > 0:
                                    board[2 - i + shift][j] = board[2 - i][j]
                                    board[2 - i][j] = 0
                                if 3 - i + shift <= 3:
                                    if board[2 - i + shift][j] == board[3 - i + shift][j] and not merged[3 - i + shift][j] \
                                            and not merged[2 - i + shift][j]:
                                        board[3 - i + shift][j] *= 2
                                        score += board[3 - i + shift][j]
                                        board[2 - i + shift][j] = 0
                                        merged[3 - i + shift][j] = True

                    elif direc == 'LEFT':
                        for i in range(4):
                            for j in range(4):
                                shift = 0
                                for q in range(j):
                                    if board[i][q] == 0:
                                        shift += 1
                                if shift > 0:
                                    board[i][j - shift] = board[i][j]
                                    board[i][j] = 0
                                if board[i][j - shift] == board[i][j - shift - 1] and not merged[i][j - shift - 1] \
                                        and not merged[i][j - shift]:
                                    board[i][j - shift - 1] *= 2
                                    score += board[i][j - shift - 1]
                                    board[i][j - shift] = 0
                                    merged[i][j - shift - 1] = True

                    elif direc == 'RIGHT':
                        for i in range(4):
                            for j in range(4):
                                shift = 0
                                for q in range(j):
                                    if board[i][3 - q] == 0:
                                        shift += 1
                                if shift > 0:
                                    board[i][3 - j + shift] = board[i][3 - j]
                                    board[i][3 - j] = 0
                                if 4 - j + shift <= 3:
                                    if board[i][4 - j + shift] == board[i][3 - j + shift] and not merged[i][4 - j + shift] \
                                            and not merged[i][3 - j + shift]:
                                        board[i][4 - j + shift] *= 2
                                        score += board[i][4 - j + shift]
                                        board[i][3 - j + shift] = 0
                                        merged[i][4 - j + shift] = True
                    return board


                # spawn in new pieces randomly when turns start
                def new_pieces(board):
                    count = 0
                    full = False
                    while any(0 in row for row in board) and count < 1:
                        row = random.randint(0, 3)
                        col = random.randint(0, 3)
                        if board[row][col] == 0:
                            count += 1
                            if random.randint(1, 10) == 10:
                                board[row][col] = 4
                            else:
                                board[row][col] = 2
                    if count < 1:
                        full = True
                    return board, full


                # draw background for the board
                def draw_board():
                    pygame.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)
                    score_text = font.render(f'Score: {score}', True, 'black')
                    high_score_text = font.render(f'High Score: {high_score}', True, 'black')
                    screen.blit(score_text, (10, 410))
                    screen.blit(high_score_text, (10, 450))
                    pass


                # draw tiles for game
                def draw_pieces(board):
                    for i in range(4):
                        for j in range(4):
                            value = board[i][j]
                            if value > 8:
                                value_color = colors['light text']
                            else:
                                value_color = colors['dark text']
                            if value <= 2048:
                                color = colors[value]
                            else:
                                color = colors['other']
                            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
                            if value > 0:
                                value_len = len(str(value))
                                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                                value_text = font.render(str(value), True, value_color)
                                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                                screen.blit(value_text, text_rect)
                                pygame.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)


                # main game loop
                run = True
                while run:
                    timer.tick(fps)
                    screen.fill('gray')
                    draw_board()
                    draw_pieces(board_values)
                    if spawn_new or init_count < 2:
                        board_values, game_over = new_pieces(board_values)
                        spawn_new = False
                        init_count += 1
                    if direction != '':
                        board_values = take_turn(direction, board_values)
                        direction = ''
                        spawn_new = True
                    if game_over:
                        draw_over()
                        if high_score > init_high:
                            file = open('high_score', 'w')
                            file.write(f'{high_score}')
                            file.close()
                            init_high = high_score

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_UP:
                                direction = 'UP'
                            elif event.key == pygame.K_DOWN:
                                direction = 'DOWN'
                            elif event.key == pygame.K_LEFT:
                                direction = 'LEFT'
                            elif event.key == pygame.K_RIGHT:
                                direction = 'RIGHT'

                            if game_over:
                                if event.key == pygame.K_RETURN:
                                    board_values = [[0 for _ in range(4)] for _ in range(4)]
                                    spawn_new = True
                                    init_count = 0
                                    score = 0
                                    direction = ''
                                    game_over = False

                    if score > high_score:
                        high_score = score

                    pygame.display.flip()
                pygame.quit()

            elif 'open notepad' in self.work:
                speak("opening app")
                path="C:\\Windows\\System32\\notepad.exe"
                os.startfile(path)

            elif 'switch the window' in self.work:
                import time
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')
            elif 'tell me news' in self.work:
                #news()
                speak("for speaking indian news speak india else do not speak ")
                n=self.takevoicecommand()
                if n=="india":
                    speak("please wait ,i am fetching todays india's latest five news")
                    ne()
                else:
                    speak("please wait ,i am fetching todays world's latest five news")
                    news()
            
            
                

            
            



                
            elif 'open code' in self.work:
                speak("opening app")
                codePath = "C:\\Users\\BRT301T\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)


                
            elif 'close code ' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM Code.exe ")

            elif 'close notepad' in self.work or 'close it' in self.work:
                speak("closing app")
                os.system("TASKKILL /F /IM notepad.exe")
            elif 'how to ' in self.work:
                
                
                op=self.work.replace("how to ",'')
                #opp=str('how to make'+op)
                speak("Getting Data From The Internet !")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                
                speak(how_to_func[0].summary)

            elif 'mail of dev' in self.work or 'send my mail' in self.work:
                try:
                    speak("do you have any attachment? if you have speak yes ")
                   
                    att=self.takevoicecommand()
                    if 'yes' in att:
                        email_list = {
                            'dude': 'vaidyadev2@gmail.com',
                            'friend': 'ramilajoshi1699@gmail.com',
                            
                        }
                        emaill='vaidyadev39@gmail.com'
                        pas='iuwiogwurrigcreu'

                        speak('sir,To Whom you want to send email')
                        
                        namee = self.takevoicecommand()

                        receiver = email_list [namee]
                        print(receiver)
                        speak('Okay sir!What is the subject of your email?')
                        subject = self.takevoicecommand()
                        
                        speak('And sir!Tell me the content of your email')
                        message = self.takevoicecommand ()
                        
                        
                    
                        speak("Please Enter the path of file separated with double foreward slashes without inverted comma:")
                        n=input("Please Enter your path here:")
                        speak('please wait i am sending your email')
                        email = MIMEMultipart()
                        email['From'] = emaill
                        email['To'] = receiver
                        email['Subject'] = subject
                        
                        email.attach(MIMEText(message,'plain'))
                        
                        
                        #set up the attechment
                        filename=os.path.basename(n)
                        attachment=open(n,'rb')
                        part=MIMEBase('application','octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition','attachment;filename= %s'% filename)
                        email.attach(part)
                        #####Attach the Attachment to MIMEMultipart
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        # Make sure to give app access in your Google account
                        server.login(emaill,pas)
                        text=email.as_string()
                        server.sendmail(emaill,receiver,text)
                        server.quit()
                        speak('sir Your email has been sent')
                        
                    else:
                        email_list = {
                            'dude': 'vaidyadev2@gmail.com',
                            'friend': 'ramilajoshi1699@gmail.com',}
                        emaill='vaidyadev39@gmail.com'
                        pas='iuwiogwurrigcreu'
                    


                        speak('sir,To Whom you want to send email')
                        
                        namee = self.takevoicecommand()
                        

                        receiver = email_list [namee]
                        print(receiver)
                        speak('Okay sir What is the subject of your email?')
                        subject = self.takevoicecommand()
                        speak('And sir Tell me the content of your email')
                        
                        message = self.takevoicecommand ()
                        speak("plese wait i am sending your email")
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        # Make sure to give app access in your Google account
                        server.login(emaill,pas)
                        email = EmailMessage()
                        email['From'] = emaill
                        email['To'] = receiver
                        email['Subject'] = subject
                        server.send_message(email)
                        server.quit()
                        speak('sir Your email has been sent')
                        
                        
                    
                except Exception as e:
                    pass
                    print(e)
                    speak("Sorry sir.I am not able to send this email")
            elif 'translator' in self.work or 'translate' in self.work:
                Tran()

            elif 'video downloader' in self.work or 'download youtube video' in self.work:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("Youtube Video Downloader")
                speak("Enter Video Url Here !")
                Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
                link = StringVar()
                Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
                Entry(root,width = 70,textvariable = link).place(x=32,y=90)

                def VideoDownloader():
                    url = YouTube(str(link.get()))
                    video = url.streams.get_highest_resolution()
                    video.download()
                    Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

                Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

                root.mainloop()
                speak("Video Downloaded")

            elif 'dictionary' in self.work:
                self.dict()

                
            elif'bye' in self.work or 'sleep now' in self.work :
                speak('bye sir.. see you again')
                break
            

                
            else:
                speak('i cannot understand please speak again')
startexecution= MainThread()
class Main(QMainWindow):

    def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.startTask)
            self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

        # def run(self):
        #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startexecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        
        self.ui.textBrowser_2.setText(label_time)
       
    '''def terminalprint(self, text):
        self.ui.textBrowser_3.insertPlainText(text)'''
app = QApplication(sys.argv)
jarvis = Main()
ui=Main()
jarvis.show()
exit(app.exec_())                           
