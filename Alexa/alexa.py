import webbrowser
import time
import os
import playsound
from gtts import gTTS
import speech_recognition as sr
import pyautogui
import sys




class Alexa():
    
    
    def __init__(self):
        pass
    
    def text_to_sound(self,text,filename):
        sound=gTTS(text=text,lang='ar',slow='False')
        sound.save(filename)
        
    def Alexa_Speak(self,filename):
        playsound.playsound(filename)


    def Alexa_recognize_speech(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak something...")
            audio = r.listen(source,phrase_time_limit=5)
        
        try:
            print("Recognizing...")
            text = r.recognize_google(audio,language='ar')
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return 0
        except sr.RequestError as e:
            print(f"Error fetching results; {e}")

    def find_words(self,words,speech):
        for word in words:
            if(word in speech):
                return True
        return False

    def Alexa_GM(self):
        self.text_to_sound("صباح الخير يا عمر","my_file.mp3")
        self.Alexa_Speak("my_file.mp3")
        os.system("rm my_file.mp3")
        
    def Alexa_TD(self,x):
        current_time_struct = time.localtime()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time_struct)
        day=formatted_time.split()[0]
        t=formatted_time.split()[1]
        if(x=='D'):
            self.text_to_sound("اليوم هو "+day,"my_file.mp3")
        elif(x=='T'):
            self.text_to_sound("الساعة هي "+t,"my_file.mp3")
        self.Alexa_Speak("my_file.mp3")
        os.system("rm my_file.mp3")
        
    def Alexa_Open_CGPT(self):
        webbrowser.get('firefox').open("https://chatgpt.com/")
        
    def Alexa_Open_VSCODE(self):
        os.system("code")
    
    def Alexa_Terminal(self):
        pyautogui.hotkey('ctrl','alt','t')
        
    def Alexa_GIT_Commit(self):
        os.system("cd /home/omar_tal3at/Emb_Linux/tasks/Python")
        os.system("git add -A")
        os.system('git commit -m "alexa auto commit"')
        os.system("git branch -M main")
        os.system("git remote add origin repo https://github.com/Omar-Talaat11/Python-practice.git")
        os.system("git push -u origin main")
        
    def Alexa_Open_GIT(self):
        webbrowser.get('firefox').open("https://github.com/Omar-Talaat11")
        
    def Alexa_Bye(self):
        self.text_to_sound(" مع السلامة يا عمر","my_file.mp3")
        self.Alexa_Speak("my_file.mp3")
        os.system("rm my_file.mp3")
        sys.exit()
        
        
        
        
        
    def Alexa_Respond(self,speech):
        if(self.find_words(["صباح","خير"],speech)):
            self.Alexa_GM()
            
        if(self.find_words(["يوم","تاريخ","النهارده"],speech)):
            self.Alexa_TD('D')
        
        if(self.find_words(["الساعه","الوقت"],speech)):
            self.Alexa_TD('T')
             
        if(self.find_words(["شات","ج ب ت"],speech)):
            self.Alexa_Open_CGPT()
            
        if(self.find_words(["الكود"],speech)):
            self.Alexa_Open_VSCODE()
        
        if(self.find_words(["تيرمينال"],speech)):
            self.Alexa_Terminal()
            
        if(self.find_words(["كوميت","كومنت"],speech) and self.find_words(["جيت","جيتهب"],speech)):
            self.Alexa_GIT_Commit()
            
        if(self.find_words(["افتح"],speech) and self.find_words(["جيت","جيتهب"],speech)):
            self.Alexa_Open_GIT()
            
        if(self.find_words(["سلام","مع السلامة"],speech)):
            self.Alexa_Bye()
    

        
    



alexa=Alexa()

while 1:
    recognizer = sr.Recognizer()
    alexa=Alexa()
    recognized_text = alexa.Alexa_recognize_speech()
    if(recognized_text):
        alexa.Alexa_Respond(recognized_text)