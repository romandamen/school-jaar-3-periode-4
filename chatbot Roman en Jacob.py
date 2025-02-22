import sys
import time
import random
import pyglet
from termcolor import colored, cprint
import NLdictionary as NL
import USdictionary as US
import re
import pymysql
from googletrans import Translator
import bcrypt


print("connecting", end='')
time.sleep(0.7)
print(".", end='');time.sleep(0.7);print(".", end='');time.sleep(0.6);print(".", end='');time.sleep(0.6);print(".", end='');time.sleep(0.5);print(".", end='');time.sleep(0.5);print(".", end='');time.sleep(0.4);print(".", end='');time.sleep(0.4);print(".", end='');time.sleep(0.3);print(".", end='');time.sleep(0.3);print(".", end='');time.sleep(0.2);print(".", end='');time.sleep(0.2);print(".", end='');time.sleep(0.1);print(".", end='');time.sleep(0.1);print(".", end='');time.sleep(0.05);print(".", end='');time.sleep(0.05);print(".", end='');time.sleep(0.05);print(".", end='');time.sleep(0.05);print(".", end='');time.sleep(0.05);print(".", end='');time.sleep(0.01);print(".", end='');time.sleep(0.01);print(".", end='');time.sleep(0.01);print(".", end='');time.sleep(0.01);print(".", end='');time.sleep(0.01);print(".", end='');time.sleep(0.01);print("o", end='');time.sleep(0.01);print("o", end='');time.sleep(0.01);print("o", end='');time.sleep(0.01);print("o", end='')
for i in range(0,1000,1):
    i= random.randint(0,1)
    print(i, end='')
    
connection = pymysql.connect(host="localhost",user="root",passwd="",database="chatman" )
cursor = connection.cursor()
time.sleep(0.1);print("y", end='');time.sleep(0.1);print("o", end='');time.sleep(0.1);print("u", end='');time.sleep(0.1);print(" ", end='');time.sleep(0.1);print("a", end='');time.sleep(0.1);print("r", end='');time.sleep(0.1);print("e", end='');time.sleep(0.1);print(" ", end='');time.sleep(0.1);print("c", end='');time.sleep(0.1);print("o", end='');time.sleep(0.1);print("n", end='');time.sleep(0.1);print("n", end='');time.sleep(0.1);print("e", end='');time.sleep(0.1);print("c", end='');time.sleep(0.1);print("t", end='');time.sleep(0.1);print("e", end='');time.sleep(0.1);print("d", end='')
print( )






def hash_wachtwoord(wachtwoord):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(6))


bestaand=0
naam=str(input("username:").capitalize())

cursor.execute("SELECT * FROM gebruiker WHERE gebruikersnaam=%s",(naam))
data="error"
for i in cursor:
    data=i
if data=="error":
    print("")
else:
    keuze=input("User already exist, login? y/n")
    bestaand=1

if bestaand==0:
    geboortedatum=str(input("born(JJJJ-MM-DD):"))
    password=str(input("super secret password:"))
    hashed = hash_wachtwoord(password)

    cursor.execute("""INSERT INTO gebruiker (gebruikersnaam, geboortedatum, wachtwoord) VALUES (%s,%s,%s)""", (naam, geboortedatum, hashed))
    connection.commit()
if bestaand==1:
    if keuze=="y":
        password=str(input("super secret password:"))
        print("password matches")
    else: naam="niet ingelogd"          
connection.close()







language = input("Which language do you speak: dutch or english? \n").lower()
if language == "dutch" or language == "english":
    print("\n")
else:
    print("I can't speak that language.")
    language = input("Which language do you speak: dutch or english? \n").lower()
    if language == "dutch" or language == "english":
        print("\n")
    else:
        print("I can't speak that language.")
        language = input("Which language do you speak: dutch or english? \n").lower()



try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")


def ep():
    time.sleep(0.06)

if language == "dutch":

    def translate(phrase):
        print("\n")
        text = input("Welke zin wil je vertalen?\n")

        languagetrans = input("Naar welke taal?\n").capitalize()

        destination_languages = {
            'Spaans': 'es',
            'Chinees': 'zh-CN',
            'Italiaans': 'it',
            'Hindi': 'hi',
            'Mongools': 'mn',
            'Russisch': 'ru',
            'Ukraïens': 'uk',
            'Frans': 'fr',
            'Indonesisch': 'id',
            'Japans': 'ja',
            'Slowakijns': 'sk'
        }

        if languagetrans in destination_languages:
            print("ok\n")
        else:
            print("Ik kan die taal niet spreken.\n")
            languagetrans = input("Naar welke taal?\n").capitalize()
            if languagetrans in destination_languages:
                print("ok\n")
            else:
                print("Ik kan die taal niet spreken.\n")
                languagetrans = input("naar welke taal?\n").capitalize()

        translator = Translator()

        print(translator.translate(text, dest=destination_languages[languagetrans]).text)

    def swap_pronouns(phrase):
        if 'ik ' in phrase:
            phrase = re.sub('ik ', 'jij ', phrase)
        if 'ben ' in phrase:
            phrase = re.sub('ben ', 'bent ', phrase)
        if "voel " in phrase:
            phrase = re.sub("voel ", "voelt ", phrase)
        if 'mijn ' in phrase:
            phrase = re.sub('mijn ', 'jouw ', phrase)
        if 'mij ' in phrase:
            phrase = re.sub('mij ', 'je ', phrase)
        return phrase


        
    def gevoelens(phrase):
        pattern = 'ik voel mij (.*)'
        pattern2 = 'het gaat (.*)'
        
        match = re.search(pattern, phrase)
        if not match:
            match = re.search(pattern2, phrase)
            
        if match:
            return match.group(1)
        else:
            phrase = "zo"
            return phrase
        
    def tijdprint():
        tijd = time.strftime("%H:%M:%S")
        color.write(tijd,"STRING")
        ep()
        color.write(")","STRING")
        ep()
    
    def wacht_gelezen():
        eerste = "afgeleverd ("
        tweede = "gezien ("
        for letter in eerste:
            color.write(letter,"STRING")
            ep()
        tijdprint()
        color.write(", ","STRING")
        time.sleep(0.4)
        for letter in tweede:
            color.write(letter,"STRING")
            ep()
        tijdprint()
        
    def respond(message):
        wacht_gelezen()
        print(" ")
        global naam
        if message.endswith("?"):
            if not message in NL.responses:
                if message.startswith("waarom"):
                    print(" ")
                    print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
                    delay_print("Dat weet ik niet.",0.05)
                if message.startswith("wat vind je van") or message.startswith ("wat vind jij van") or message.startswith("wat is jouw mening over"):
                    print(" ")
                    print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
                    delay_print(random.choice(NL.responses["mening"]),0.05)
                if message.startswith("ben") or message.startswith("kan") or message.startswith("hou") or message.startswith("wil") or message.startswith("doe") or message.startswith("gaat") or message.startswith("heb") or message.startswith("is") or message.startswith("moet") or message.startswith("zal"):
                    print(" ")
                    print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
                    delay_print(random.choice(NL.responses["gesloten"]),0.05)    
                else:
                    if message.startswith("wat vind je van") or message.startswith ("wat vind jij van") or message.startswith("wat is jouw mening over"):
                        pass
                    elif not message.startswith('waarom'):
                        print(" ")
                        print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
                        delay_print(random.choice(NL.responses["question"]),0.05)
        if message in NL.responses:
            if not message == "matrix":
                print(" ")
                print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
                delay_print(random.choice(NL.responses[message]),0.05)
            else:
                print(" ")
                print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
                delay_print(random.choice(NL.responses[message]),0.000)
        if not message.endswith("?"):
            if not message in NL.responses:
                if message == "vertaal":
                    translate(message)
                elif message.startswith("ik ben") or message.startswith("mijn") or message.startswith("ik voel"):
                    print(" ")
                    print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
                    delay_print(swap_pronouns(message).capitalize() + "?",0.05)
                    
                else:
                    print(" ")
                    print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
                    delay_print(random.choice(NL.responses["statement"]),0.05)
                
if language == "english":
    def translate(phrase):
        print("\n")
        text = input("What do you want to translate?\n")

        languagetrans = input("To what language do you want to translate it?\n").capitalize()

        destination_languages = {
            'Spanish': 'es',
            'Chinese': 'zh-CN',
            'Italian': 'it',
            'Hindi': 'hi',
            'Mongolian': 'mn',
            'Russian': 'ru',
            'Ukrainian': 'uk',
            'French': 'fr',
            'Indonesian': 'id',
            'Japanese': 'ja',
            'Slovak': 'sk'
        }

        if languagetrans in destination_languages:
            print("ok\n")
        else:
            print("I dont speak that language.\n")
            languagetrans = input("To what language do you want to translate it?\n").capitalize()
            if languagetrans in destination_languages:
                print("ok\n")
            else:
                print("I dont speak that language.\n")
                languagetrans = input("To what language do you want to translate it?\n").capitalize()

        translator = Translator()

        print(translator.translate(text, dest=destination_languages[languagetrans]).text)
    def swap_pronouns(phrase):
        if 'i ' in phrase:
            phrase = re.sub('i ', 'you ', phrase)
        if 'am ' in phrase:
            phrase = re.sub('am ', 'are ', phrase)
        if "i'm " in phrase:
            phrase = re.sub("i'm ", "you're ", phrase)
        if 'my ' in phrase:
            phrase = re.sub('my ', 'your ', phrase)
        return phrase

    def gevoelens(phrase):
        pattern = "im feeling (.*)"
        pattern2 = "its going (.*)"
        pattern3 = "it's going (.*)"
        pattern4 = "it is going (.*)"
        pattern5 = "i'm feeling (.*)"
        pattern6 = "i am feeling (.*)"        
        
        match = re.search(pattern, phrase)
        if not match:
            match = re.search(pattern2, phrase)
            if not match:
                match = re.search(pattern3, phrase)
                if not match:
                    match = re.search(pattern4, phrase)
                    if not match:
                        match = re.search(pattern5, phrase)
                        if not match:
                            match = re.search(pattern6, phrase)
        if match:
            return match.group(1)
        else:
            phrase = "that way"
            return phrase

    def naam_begin(name):
        global naam
        letters = 0
        for char in name:
            letters+=1
        if letters >= 15:
            print(" ")
            print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
            delay_print("That looks a little bit too long for me.",0.05)
            delay_print("Who are you really?",0.05)
            print(" ")
            naam = input('')
            naam_begin(naam)
        if letters <= 15:
            print(" ")
            print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
            delay_print("Oh ofcourse.",0.05)
            
    def tijdprint():
        tijd = time.strftime("%I:%M:%S %p")
        color.write(tijd,"STRING")
        ep()
        color.write(")","STRING")
        ep()
        
    def wacht_gelezen():
        eerste = "delivered ("
        tweede = "seen ("
        for letter in eerste:
            color.write(letter,"STRING")
            ep()
        tijdprint()
        color.write(", ","STRING")
        time.sleep(0.4)
        for letter in tweede:
            color.write(letter,"STRING")
            ep()
        tijdprint()
        
    def respond(message):
        wacht_gelezen()
        print(" ")
        global naam
        
        if message.endswith("?"):
            if not message in US.responses:
                if message.startswith("why"):
                    print(" ")
                    print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
                    delay_print("I don't know.",0.05)
                if message.startswith("what are your thoughts on") or message.startswith ("what do you think of") or message.startswith("what is your opinion about") or message.startswith("What is your opinion on"):
                    print(" ")
                    print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
                    delay_print(random.choice(US.responses["opinion"]),0.05)
                if message.startswith("are") or message.startswith("can") or message.startswith("do you like") or message.startswith("Do you want") or message.startswith("do") or message.startswith("is it going") or message.startswith("do you have") or message.startswith("is"):
                    print(" ")
                    print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
                    delay_print(random.choice(US.responses["closed"]),0.05)    
                else:
                    if message.startswith("what are your thoughts on") or message.startswith ("what do you think of") or message.startswith("what is your opinion about") or message.startswith("What is your opinion on"):
                        pass
                    elif not message.startswith('why'):
                        print(" ")
                        print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
                        delay_print(random.choice(US.responses["question"]),0.05)
        if message in US.responses:
            if not message == "matrix":
                print(" ")
                print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
                delay_print(random.choice(US.responses[message]),0.05)
            else:
                print(" ")
                print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
                delay_print(random.choice(US.responses[message]),0.000)
        if not message.endswith("?"):
            if not message in US.responses:
                if message == "translate":
                    translate(message)
                elif message.startswith("i am") or message.startswith("my") or message.startswith("im") or message.startswith("i'm") or message.startswith("i feel"):
                    print(" ")
                    print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
                    delay_print(swap_pronouns(message).capitalize() + "?",0.05)
                    
                else:
                    print(" ")
                    print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
                    delay_print(random.choice(US.responses["statement"]),0.05)
                            
def delay_print(string, speed):
    drie = 2
    length = 0
    for char in string:
        length += 1
    if length >= 10:
        speed = 0.03
    for char in string:
        print(char, end='')
        drie += 1
        time.sleep(speed)
        if drie == 3:
            sound = pyglet.media.load('type.ogg', streaming=False)
            sound.play()
            drie = 0
    print("                 ")

    
if language == "dutch":    

    color.write("|||4G                                  " + time.strftime("%H:%M") + "                                60%","BUILTIN")
    color.write("  _____________________________________________________________________________ \n","BUILTIN")
    color.write("|Spreekbot                                                                    |\n","BUILTIN")
    color.write("|Tik voor contactinformatie.                                                  |\n","BUILTIN")
    color.write("|_____________________________________________________________________________|\n","BUILTIN")
    print(" ")
    print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
    delay_print("Hoe voel je je " + naam + "?",0.05)
    print(" ")
    color.write(time.strftime("%H:%M:%S") + ", " + naam + ':',"STRING")
    gevoel = str(input("  ").lower())
    print(" ")
    print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
    delay_print("Waarom voel je je {}?".format(gevoelens(gevoel)),0.05)
    print(" ")
    color.write(time.strftime("%H:%M:%S") + ", " + naam + ':',"STRING")
    input("  ")
    print(" ")
    print(time.strftime("%H:%M:%S") + ", " + "Spreekbot")
    delay_print("Oke, als er ooit iets is wat ik voor je kan doen, dan moet je het zeggen.",0.05)
    
if language == "english":

    color.write("|||4G                                  " + time.strftime("%H:%M") + "                                60%","BUILTIN")
    color.write("  _____________________________________________________________________________ \n","BUILTIN")
    color.write("|Chatbot                                                                      |\n","BUILTIN")
    color.write("|Tap for contactinformation.                                                  |\n","BUILTIN")
    color.write("|_____________________________________________________________________________|\n","BUILTIN")
    print(" ")
    print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
    delay_print("Have a new phone, who is this?",0.05)
    print(" ")
    naam= input('')
    naam_begin(naam)
    print(" ")
    print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
    delay_print("How are you feeling " + naam + "?",0.05)
    print(" ")
    color.write(time.strftime("%I:%M:%S %p") + ", " + naam + ':',"STRING")
    gevoel = str(input("  ").lower())
    print(" ")
    print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
    delay_print("Why are you feeling {}?".format(gevoelens(gevoel)),0.05)
    color.write(time.strftime("%I:%M:%S %p") + ", " + naam + ':',"STRING")
    input("  ")
    print(" ")
    print(time.strftime("%I:%M:%S %p") + ", " + "Chatbot")
    delay_print("Okay, if there's anything i could help you with, you can say it.",0.05)   



while True:
    if language == "dutch":
        print(" ")
        color.write(time.strftime("%H:%M:%S") + ", " + naam + ':',"STRING")
        antwoord = input(' ').lower()
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        respond(antwoord)
            
    if language == "english":
        print(" ")
        color.write(time.strftime("%I:%M:%S %p") + ", " + naam + ':',"STRING")
        antwoord = input(' ').lower()
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        if antwoord.endswith('.'):
            antwoord = antwoord[:-1]
        respond(antwoord)
