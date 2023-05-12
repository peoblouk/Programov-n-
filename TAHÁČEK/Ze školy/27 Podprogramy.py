# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:33:14 2013


"""

"""

PODPROGRAM

Výhody:
    1) Přehlednost
    2) Opakované použití - ušetříme psaní

Syntaxe:
def Název (parametr1,parametr2,...):
    blok příkazů
    return vásledný výraz
    
Pozn. Poekud neuvedeme return, vrací se vždy None

Počet parametrů:
    a) žádné            def Fce()
    b) konkrétní počet  def Fce(x,y,z)
    c) proměnlivý počet def Fce(x,*parametr)
    
Implicitní hodnoty parametrů:
    V definici funkce může být do parametru
    předána implicitní hodnota, která se použije
    v prípadě, že tento parametr nebude dosazen.
!!! Všechny parametry vpravo od něj musí být také implicitní !!!

"""

def Pozdrav():
    print u"Dobré ráno"

#Pozdrav()    

    
def Pozdravy(pocet):
    for i in range(pocet):
        print "Hellooooo!"

#Pozdravy(5)


def SuperPozdrav(pocet,text):
    for i in range(pocet):
        print text
        
#SuperPozdrav(5,u"Zdááár")
#SuperPozdrav(3,"Pako")


def Mocnina(x):
    return x**2

#print Mocnina(7)


def PokusParametry1(x,*par):
    print x
    print par
    
#PokusParametry1(100, "Patek", "Sobota", "Nedele")


def PokusParametry2(x,y=100,*z):
    print x
    print y
    print z

#PokusParametry2(50,1,3,5,7)


def Vypis(x,*parametry):
    print x
    print parametry
    for i in parametry:
        print i
        
#Vypis(100,"nic","true",[1,4])

