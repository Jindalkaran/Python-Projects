import pyttsx3#text to speech
import wikipedia
import datetime
import wolframalpha
import os
import sys
import webbrowser
import smtplib#server for sending gmail... If you want to retrieve email instead, then  check out the IMAP 
import random
import speech_recognition as sr
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By


#https://youtu.be/5mu6qlFY3x0
# for making exe type in cmd :pyinstaller --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 --onefile JARVIS.py


def speak(text):#function to speak text
    print('Computer: ' + text)
    engine.say(text)
    engine.runAndWait()
    
def greet():
    hour= int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')

    if hour >= 12 and hour < 18:
        speak('Good Afternoon!')

    if hour >= 18 and hour !=0:
        speak('Good Evening!')

def get_Command():#function for audio to text from microphone
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
       speak('Sorry sir! I didn\'t get that! Try typing the command!')
       query = str(input('Command: '))
    return query

        





if __name__ == '__main__':
    driver=webdriver.Chrome("C:/Users/karan/Documents/Pythons/NEPPTEL/chromedriver")#webdriver to drive browser
    client = wolframalpha.Client('XR4XAV-7THJE4VQ4R')#for searching web
    #making an engine/object for text to speech
    engine = pyttsx3.init('sapi5')#sapi is microsoft api  inbuilt for text to speech
    voices_in_pc= engine.getProperty('voices')#differnt voices present in engine, here 2
    print(voices_in_pc)
    engine.setProperty('voice', voices_in_pc[1].id)#select a voice
    greet()
    speak('Hello Sir, I am your personal digital assistant ')
    speak('How may I help you ?')


    while True:
        query = get_Command().lower();
        
        if 'open youtube' in query:
            speak('okay !! Opening Youtube')
            webbrowser.open('www.youtube.com')

        elif 'open facebook' in query:
            speak('okay !! Opening facebook')
            webbrowser.open('https://www.facebook.com/')

        elif 'open google' in query:
            speak('okay !! Opening google')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay ! Opening gmail')
            webbrowser.open('www.gmail.com')

        elif "what\s up" in query or 'how are you' in query or 'whats up' in query:
            Msgs = ['Just doing my thing! I am fine!', 'I am nice and full of energy']
            speak(random.choice(Msgs))

        elif 'open camera' in query:
            os.startfile('C:\\Users\\karan\\Desktop\\Camera.lnk')

        elif 'send message on whatsapp' in query:
            speak('Who is the recipient? ')
            recipient = get_Command()
            speak('What should I say? ')
            content = get_Command()
            driver.get("https://web.whatsapp.com")
            try:
                alert = browser.switch_to_alert()
                alert.accept()
            except:
                print ("no alert")
            time.sleep(5)
            search_box= driver.find_element_by_class_name('_2zCfw')
            search_box.send_keys(recipient+Keys.ENTER)
            for i in range(20):
                text_box= driver.find_element_by_class_name('_3u328' )
                text_box.send_keys(content+Keys.ENTER)

        elif 'login to google' in query:
            speak('wait...')
            driver.get('https://accounts.google.com/ServiceLogin?service=CPanel')
            speak('give your email')
            email=get_Command()
            speak('give google password')
            password=get_Command()
            driver.find_element_by_id("identifierId").send_keys(email)
            driver.find_element_by_id("identifierNext").click()
            time.sleep(2)
            driver.find_element_by_name("password").send_keys(password)
            driver.find_element_by_id("passwordNext").click()
            speak('You are logged in')
            

        

        elif 'send email' in query:
            speak('Who is the recipient? ')
            recipient = get_Command()
            try:
                speak('What should I say? ')
                content = get_Command()
                #using smtplib library
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login("karanagarwal429@gmail.com", '')#allow less secure apps in your google settings from https://myaccount.google.com/security#activity
                server.sendmail("karanagarwal429@gmail.com",recipient, content)#mail goes to spam folder so needs some work
                server.close()
                speak('Email sent!')
            except:
                speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'stop' in query or 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir !! Wish you a wonderful day')
                                    
        elif 'play music' in query:
            music_folder="C:\\Users\\karan\\Music\\English songs\\"
            musics = ['Carly', 'Hall']
            random_music = music_folder + random.choice(musics) + '.mp3'
            os.startfile(random_music)
            speak('Okay, here is your music! Enjoy!')
            

        else:
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! sir!')
