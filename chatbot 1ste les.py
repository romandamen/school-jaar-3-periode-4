import sys
import time
import random
import pyglet
from termcolor import colored, cprint
import sys
import NLdictionary as NL
import USdictionary as US
import re
language = input("Which language do you speak: dutch or english? \n")
if language == "dutch" or language == "english":
    print("\n")
else:
    print("I can't speak that language.")
    language = input("Which language do you speak: dutch or english? \n")
    if language == "dutch" or language == "english":
        print("\n")
    else:
        print("i can't speak that language.")
        language = input("Which language do you speak: dutch or english? \n")



try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
beurt = 0

def ep():
    time.sleep(0.06)

if language == "dutch":
    def swap_pronouns(phrase):
        if 'ik' in phrase:
            return re.sub('ik', 'jij', phrase)
        if 'mijn' in phrase:
            return re.sub('mijn', 'jouw', phrase)
        else:
            return phrase
        
    def gevoelens(phrase):
        pattern = 'ik voel mij (.*)'
        pattern2 = 'het gaat (.*)'
        
        match = re.search(pattern, phrase)
        match = re.search(pattern2, phrase)
        if match:
            return match.group(1)
        else:
            return phrase
            
if language == "english": 
    def swap_pronouns(phrase):
        if 'I' in phrase:
            return re.sub('I', 'you', phrase)
        if 'my' in phrase:
            return re.sub('my', 'your', phrase)
        else:
            return phrase
    
if language == "dutch":
    def naam_begin(name):
        global naam
        letters = 0
        for char in name:
            letters+=1
        if letters >= 15:
            print(" ")
            print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
            delay_print("Dat lijkt mij een beetje lang.",0.05)
            delay_print("Wie ben je echt?",0.05)
            print(" ")
            naam = input('')
            naam_begin(naam)
        if letters <= 15:
            print(" ")
            print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
            delay_print("Ohhh tuurlijk.",0.05)        
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
if language == "english":
    def naam_begin(name):
        global naam
        letters = 0
        for char in name:
            letters+=1
        if letters >= 15:
            print(" ")
            print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
            delay_print("That looks a little bit too long for me.",0.05)
            delay_print("Who are you really?",0.05)
            print(" ")
            naam = input('')
            naam_begin(naam)
        if letters <= 15:
            print(" ")
            print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
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
        
def delay_print(string, speed):
    global beurt
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
    beurt = 0

    
if language == "dutch":    
    def respond(message):
        wacht_gelezen()
        print(" ")
        global naam
        if message.endswith("?"):
            if not message in NL.responses:
                if message.startswith("waarom?"):
                    print(" ")
                    print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
                    delay_print("gewoon",0.05)
                if message.startswith("hoeveel procent"):
                    pass
                    #E= random.randint(0, 100)
                    #delay_print(time.strftime("%H:%M:%S") + ", " + "spreekbot:" + ,0.05)
                if message.startswith("wat vind je van") or message.startswith ("wat vind jij van") or message.startswith("wat is jouw mening over"):
                    print(" ")
                    print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
                    delay_print(random.choice(NL.responses["mening"]),0.05)
                if message.startswith("ben") or message.startswith("kan") or message.startswith("hou") or message.startswith("wil") or message.startswith("doe") or message.startswith("gaat") or message.startswith("heb") or message.startswith("is") or message.startswith("moet") or message.startswith("zal"):
                    print(" ")
                    print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
                    delay_print(random.choice(NL.responses["gesloten"]),0.05)    
                else:
                    if message.startswith("wat vind je van") or message.startswith ("wat vind jij van") or message.startswith("wat is jouw mening over"):
                        pass
                    else:
                        if not message.startswith('waarom'):
                            print(" ")
                            print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
                            delay_print(random.choice(NL.responses["question"]),0.05)
        if message in NL.responses:
            if not message == "matrix":
                print(" ")
                print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
                delay_print(random.choice(NL.responses[message]),0.05)
            else:
                print(" ")
                print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
                delay_print(random.choice(NL.responses[message]),0.000)
        if not message.endswith("?"):
            if not message in NL.responses:
                print(" ")
                print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
                delay_print(random.choice(NL.responses["statement"]),0.05)
                
    color.write("|||4G                                  " + time.strftime("%H:%M") + "                                60%","BUILTIN")
    color.write("  _____________________________________________________________________________ \n","BUILTIN")
    color.write("|spreekbot                                                                    |\n","BUILTIN")
    color.write("|tik voor contactinformatie                                                   |\n","BUILTIN")
    color.write("|_____________________________________________________________________________|\n","BUILTIN")
    print(" ")
    print(time.strftime("%H:%M:%S") + ", " + "spreekbot")
    delay_print("heb een nieuwe telefoon, wie is dit?",0.05)
    print(" ")
    naam= input('')
    naam_begin(naam)
    print(" ")
    print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
    delay_print("hoe gaat het " + naam + "?",0.05)
    print("\n")
    color.write(time.strftime("%H:%M:%S") + ", " + naam + ':',"STRING")
    gevoel = str(input("  "))
    print(" ")
    print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
    delay_print("waarom voel je je {}?".format(gevoelens(gevoel)),0.05)
    
if language == "english":
    def respond(message):
        wacht_gelezen()
        print(" ")
        global naam
        
        if message.endswith("?"):
            if not message in US.responses:
                if message.startswith("why?"):
                    print(" ")
                    print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
                    delay_print("Not really a reason.",0.05)
                if message.startswith("what percentage"):
                    pass
                    #E= random.randint(0, 100)
                    #delay_print(time.strftime("%I:%M:%S %p") + ", " + "spreekbot:" + ,0.05)
                if message.startswith("what are your thoughts on") or message.startswith ("what do you think of") or message.startswith("what is your opinion about") or message.startswith("What is your opinion on"):
                    print(" ")
                    print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
                    delay_print(random.choice(US.responses["meaning"]),0.05)
                if message.startswith("are") or message.startswith("can") or message.startswith("do you like") or message.startswith("Do you want") or message.startswith("do") or message.startswith("is it going") or message.startswith("do you have") or message.startswith("is"):
                    print(" ")
                    print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
                    delay_print(random.choice(US.responses["closed"]),0.05)    
                else:
                    if message.startswith("what do you think of") or message.startswith("what is your opinion about"):
                        pass
                    else:
                        if not message.startswith('why'):
                            print(" ")
                            print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
                            delay_print(random.choice(US.responses["question"]),0.05)
        if message in US.responses:
            if not message == "matrix":
                print(" ")
                print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
                delay_print(random.choice(US.responses[message]),0.05)
            else:
                print(" ")
                print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
                delay_print(random.choice(US.responses[message]),0.000)
        if not message.endswith("?"):
            if not message in US.responses:
                print(" ")
                print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
                delay_print(random.choice(US.responses["statement"]),0.05)
                    
    color.write("|||4G                                  " + time.strftime("%H:%M") + "                                60%","BUILTIN")
    color.write("  _____________________________________________________________________________ \n","BUILTIN")
    color.write("|chatbot                                                                      |\n","BUILTIN")
    color.write("|tap for contactinformation                                                   |\n","BUILTIN")
    color.write("|_____________________________________________________________________________|\n","BUILTIN")
    print(" ")
    print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
    delay_print("have a new phone, who is this?",0.05)
    print(" ")
    naam= input('')
    naam_begin(naam)
    print(" ")
    print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
    delay_print("how are you feeling" + naam + "?",0.05)
    print("\n")
    color.write(time.strftime("%H:%M:%S") + ", " + naam + ':',"STRING")
    print(gevoelens(input(" ")))



while True:
    if language == "dutch":
        if beurt == 0:
            beurt = 1
            print(" ")
            color.write(time.strftime("%H:%M:%S") + ", " + naam + ':',"STRING")
            respond(input(' '))
            
    if language == "english":
        if beurt == 0:
            beurt = 1
            print(" ")
            color.write(time.strftime("%I:%M:%S %p") + ", " + naam + ':',"STRING")
            respond(input(' '))
