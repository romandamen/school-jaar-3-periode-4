naam = " "
import sys
import time
import random
import pyglet
from termcolor import colored, cprint
import sys
import NLdictionary as NL
responses = {
        "hoe heet je?": ["Ik ben Spreekbot."],
        "wat voor weer is het?": ["Het weer is vandaag wel goed.","Niet zo goed."],
        "wat is het weer?": ["Het weer is vandaag wel goed.","Niet zo goed."],
        "hoe is het weer?": ["Het weer is vandaag wel goed.","Niet zo goed."],
        "wat voor weer is het vandaag?": ["Het weer is vandaag wel goed.","Niet zo goed."],
        "steen": ["Steen, Gelijkspel!","Papier, ik win!","Schaar, goed gespeeld!" + naam],
        "papier": ["Steen, goed gespeeld! " + naam,"Papier, gelijkspel!","Schaar, ik win!"],
        "schaar": ["Steen, ik win!","Papier, goed gespeeld!." + naam,"Schaar, gelijkspel!"],
        "gooi een muntje": ["Kop!","Munt!"],
        "gooi een munt": ["Kop!","Munt!"],
        "hoi": ["Hey " + naam + "!","Hey!"],
        "hallo": ["Hey " + naam + "!","Hey!"],
        "hey": ["Hey " + naam + "!","Hey!"],
        "goedemorgen": ["Hey " + naam + "!","Hey!"],
        "matrix": ["10010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001100101010100010001010010010010010010010010010010000101010011101010010100100111010101001001010101010101011010101010010101010101011010101111010111010111101101010101000101101010001101010100101010010010010100101010101010101010101010110101010101101010101010101010010010010010100101010010100110010101010001000101001001001001001001001001001000010101001110101001010010011101010100100101010101010101101010101001010101010101101010111101011101011110110101010100010110101000110101010010101001001001010010101010101010101010101011010101010110101010101010101001001001001010010101001010011001010101000100010100100100100100100100100100100001010100111010100101001001110101010010010101010101010110101010100101010101010110101011110101110101111011010101010001011010100011010101001010100100100101001010101010101010101010101101010101011010101010101010100100100100101001010100101001"],
        "nee": ["Oke."],
        "nietes": ["Oke."],
        "jawel": ["Oke."],
        "ja": ["Oke."], 
        "kop of munt": ["Kop!","Munt!"],
        "hoe gaat het?": ["Goed hoor.","Wel goed.","Slecht.","Niet het beste."],
        "gaat het goed?": ["Ja hoor.","Niet echt."],
        "hoe gaat het met het leven?": ["Het gaat wel lekker.","Prima.","Niet echt goed.","Slecht."],
        "thx": ["Geen probleem."],
        "hoelaat is het?": ["Het is " + time.strftime("%H:%M:%S") + "."],
        "bedankt": ["Geen probleem."],
        "thx": ["Geen probleem."],
        "dankjewel": ["Geen probleem."],
        "oh": ["..."],
        "aii": [""],
        "ok": [""],
        "oke": [""],
        "sorry": ["Geen probleem hoor.", "Geen probleem."],
        "doei": ["Doei!", "Later!", "Fijne dag verder."],
        "statement":[
            'Hmm.'],
        "question": ["Wat?"],
        "gesloten": ["Ja.","Nee."],
        "mening": ["Goed.","Slecht.","Nooit echt over nagedacht.","Apart."]}
