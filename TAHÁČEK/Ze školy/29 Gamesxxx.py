# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 09:18:21 2013


"""
import random

def Kamen():
    print u"Kámen nůžky, papír"
    volba=input(u"Vyberte: (Kámen=1, Nůžky=2, Papír=3): ")

    if volba==1:
        print (u"Vaše volba je: Kámen")   
    elif volba==2:
        print (u"Vaše volba je: Nůžky")
    elif volba==3:
        print (u"Vaše volba je: Papír")
    else:
        print (u"Špatná hodnota")
                    
    PC=random.randint(1,3)

    if PC==1:
        print (u"Volba PC je: Kámen")   
    elif PC==2:
        print (u"Volba PC je: Nůžky")
    else:
        print (u"Volba PC je: Papír")

    if volba==PC:
        print (u"Remíza!")
    if (volba==1 and PC==2) or (volba==2 and PC==3) or (volba==3 and PC==1):
        print (u"Jsi vítěz!")    
    if (volba==1 and PC==3) or (volba==2 and PC==1) or (volba==3 and PC==2):
        print (u"Prohrál jsi!")
    print
    
    
def Cislo():
    print u"Hádej číslo"
    x=random.randint(1,100)
    tip=input(u"Zvol číslo od 1 do 100: ")

    while tip<>x:
        if tip>x:
            print u"Zadej MENŠÍ"
        
        else:
            print u"Zadej VĚTŠÍ"
        
        tip=input(u"Zvol nové číslo: ") 
    
    print("Gratulace!!!")


def Sportka():
    print u"Sportka"
    x=0
    generator=[]
    while x<6:
        cislo=random.randint(1,49)
        if generator.count(cislo)<1:
            x+=1
            generator.append(cislo)
    generator.sort()
    pocet=0
    tip=[]
    while pocet<6:
        cislo=input(u"Zadejte číslo od 1 do 49: ")
        if tip.count(cislo)<1:
            pocet+=1
            tip.append(cislo)
    tip.sort()

    print "Tip", tip
    print "Sportka", generator

    kolik=0
    for cislo in tip:
        if cislo in generator:
            kolik+=1        
    print u"Udádl jsi ",kolik, u"čísel"

volba=0
while volba<>4:
    print u"1) Kámen, nůžky, papír"
    print u"2) Hádej číslo"
    print u"3) Sportka"
    print u"4) Konec"
    volba=input("Vyber si hru: ")


if volba==1:
    print Kamen
if volba==2:  
    print Cislo
if volba==3:
    print Sportka
   
    

