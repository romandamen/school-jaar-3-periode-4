import sys
import time
import random
import pyglet
from termcolor import colored, cprint
import sys
import USdictionary as US


language = input("Which language do you speak?: Spanish, Dutch or English?   ")


try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
beurt = 0
def ep():
    time.sleep(0.06)
def naam_begin(name):
    global naam
    letters = 0
    for char in name:
        letters+=1
    if letters >= 15:
        print(" ")
        print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
        delay_print("That looks a little bit too long for me",0.05)
        delay_print("Who are you really?",0.05)
        print(" ")
        naam = input('')
        naam_begin(naam)
    if letters <= 15:
        print(" ")
        print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
        delay_print("oh",0.05)
        
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
    
def respond(message):
    wacht_gelezen()
    print(" ")
    global naam
    
    if message.endswith("?"):
        if not message in US.responses:
            if message.startswith("why?"):
                print(" ")
                print(time.strftime("%I:%M:%S %p") + ", " + "chatbot")
                delay_print("not really a reason",0.05)
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



toevoegen = []


while True:
    if beurt == 0:
        beurt = 1
        print(" ")
        color.write(time.strftime("%I:%M:%S %p") + ", " + naam + ':',"STRING")
        respond(input(' '))
