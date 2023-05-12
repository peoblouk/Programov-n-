# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 09:19:44 2012


"""
"""

SOUBORY:
- TEXTOVÉ - U čísel se zapisuje každá cifra zvlášť (1B)
          - Data jsou zapsána v řádcích (/n)     
Př: Číslo 12: TEXT > 00000001 00000010           
Přípony: *.txt   *.html   *.py     

          
- BINÁRNÍ - Čísla se zapisují binárně jako celek
          - Nejsou žádné řádky          
Př: Číslo 12: BIN  > 00001100
Přípony: *.doc   *-jpg    *-zip   



     Soubory (textové)
open(cesta,mód) - otevře soubor a nastaví způsob
                  přístupu (mód)

módy:
  'r' - otevře daný soubor pro čtení
  'r+' - otevře soubor jak pro čtení, tak pro zápis
  'w' - otevře pro zápis, neexistující soubor bude
        vytvořen, existující soub. bude přepsán
  'a' - pro zápis na konec souboru, neexistující 
        bude vytvořen      

close() - zavře soubor, způsobí uložení, uvolní jej pro jiné aplikace
write() - zapíše do souboru daný řetězec na aktuální
          pozici
flush() - vynucené uložení souboru
writelines() - zapíše do souboru seznam řádků         
readlines() - vrátí seznam řádků souboru          
readline() - přečte 1 řádek souboru  
read(x) - přečte řetězec o zadané délce
tell() - vrací aktuální pozici v souboru
seek(pocet,pozice) - posune ukazatel o daný počet
                    bitů od zadané pozice
   pozice:
    0 - začátek souboru
    1 - aktuální pozice
    2 - konec souboru                 
"""

import random

"""
soubor=open('pokus.txt','w')
soubor.write('Dnes je streda a bude obed.\n')
soubor.write('Zitra je ctvrtek.\n')
soubor.write(str(1000000))
soubor.close()

"""
"""
soubor=open('cisla.txt','w')
for i in range(1000000):
    x=random.randint(1,1000)
    soubor.write("%i\n" % x)
soubor.close()


soubor=open('pokus.txt','r+')
seznam=soubor.readlines()
print seznam
for radek in seznam:
    print radek,
    
pozice=soubor.tell()
print pozice


soubor.seek(5,0)
soubor.write('*****')


soubor.seek(0,0)
radek=soubor.readline()
print radek    

soubor.seek(0,0)
radek=soubor.read(15)
print radek    
soubor.close()
"""

"""
Úkoly:
1) Otevřete soubor pokus.txt a vypište jeho 
   obsah do souboru kopie.txt.
   
2) Vygenerujte soubor VSTUP.TXT, ve kterém budou dva
   sloupce dvojciferných čísel oddělené mezerou. V
   každém bude 100 čísel.
   Tento soubor postupně přečtěte a vypište řádkové
   součty ve formátu a+b=c.
   
3) Přečtěte soubor PISMENA.TXT znak po znaku a 
   zjistěte, kolik je v něm písmen "a".
   
4) Zapište do souboru CISLA.TXT čísla od 1 do 1000.
   (Rozšíření: ka každému číslu doplnit jeho dělitele)
   
   """
   
   
   
#1
"""
pokus=open("pokus.txt","r")
seznam=pokus.readlines()
kopie=open("kopie.txt","w")
kopie.writelines(seznam)
pokus.close()
kopie.close()
"""

#2
"""

import random
Vstup=open("vstup.txt","w")
for i in range(100):
    a=(random.randint(10,99)) 
    b=(random.randint(10,99))
    Vstup.write("%i" % a)
    Vstup.write(" %i\n" % b)
    print a, b
Vstup.close

print ""
print u"Součty:"

Vstup=open("vstup.txt","r")    
for i in range(100):
    a=int(Vstup.read(2))
    b=int(Vstup.readline())
    c=a+b
    print i+1,")",a,"+",b,"=",c
    
"""    
#3

"""
soubor=open("pismena.txt","r")  

znak=" "
pocet=0
while znak<>"":
    znak=soubor.read(1)
    if znak=="a":
        pocet+=1

soubor.close()
print "soubor obsahuje znak 'a' %ix" % pocet        
"""

#4

soubor=open("cisla.txt","w")
for i in range (1,1001):
    soubor.write("%4i: " %(i))
    for x in range (1,1000):
        if i%x==0:
            soubor.write(str(x)+" ")
    soubor.write("\n")
soubor.close()












N-tice (tuple)
- vytvářejí se pomocí ()
- jsou neměnné
- nemají žádné metody (jako např. pop(), ...)

"""
"""
tuple()
print tuple

x=(3, "ahoj", 4.7, None)
print x

print x[1]
"""

"""

Úkol:
    1) Vygenerujte seznam s 10-ti tříprvkovými n-ticemi.
       Náhodná čísla  z intervalu <0,1>, 
       Vypište n-tice pod sebou
       
"""

import random
S=[]
for i in range(10):
    S.append((random.randint(0,1),random.randint(0,1),random.randint(0,1)))
for i in S:
    print i





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




Řetězce (string)
- uzavřeny v apostrofech (') nebo v uvozovkách (")
- trojí uvozovky mohou uzavírat i více řádků

Speciální znaky - začínají lomítkem
\' - apostrof
\" - uvozovka
\\ - lomítko
\n - nový řádek

ret= r"Specialni \n znaky: \' \\ \" "
print ret
"""

"""
Formátovací operátor %
- slouží ke vkládání a formátování různých
  datových typů do řetězce
Obecně:
"...%zkratka typu ..." % (N-tice hodnot)  

Zkratky typů:
%i celé číslo
%f desetinné
%s řetězec
%x hexadecimální tvar
%o osmičkový tvar

%5.2f číslo bude složeno z 5 znaků, z toho 2
      budou za desetinnou tečkou, chybějící znaky
      budou nahrazeny mezerami zleva

%-8.2f číslo bude složeno z 8 znaků, z toho 2
      budou za desetinnou tečkou, chybějící znaky
      budou nahrazeny mezerami zprava

%4i  obdobně pro celá čísla 
%-4i
Indexování
K jednotlivým částem řetezce lze přistoupit 
pomocí [].
Kladné hodnoty číslují znaky zleva, záporné zprava.      

ret="patek"
print ret[-1]       # poseldní znak
"""

"""
Operátor : (slice)
- vrací podřetězec
[:n] - vrátí prvních n znaků
[n:] - vrátí podřetězec od pozice n do konce
[m:n] - vrátí podřetězec od pozice m do n
"""
#print ret[:3]
#print ret[-3:]
#print ret[1:3]
"""


Funkce str()
- převede libovolný typ na řetězec
"""
#sez=[1,3,8]
#ret=str(sez)
#print sez
#print ret

"""
z=24
x="Cele %4i desetinne %-8.2f text" % (z,z)
print x


w="Retezec %s retezec" % 'vlozeny text'
print w

y="Hexadecimalni %x oktalove %o" % (z,z)
print y

slovnik={'cislo':1000000,'text':'nejaky text'}
v="Slovnik %(text)s" % slovnik
print v
"""
"""
ret="Pokusny retezec"
print ret[4:10]
seznam=[3, 'three', 3.0]
ret="Cislo "+str(seznam)
print ret
"""

"""
Úkol:
1) Vypište číslo 20.14 pomocí všech možných typů (i,f,x,o,s)
2) Vypište pod sebe seznam 10 náh. čísel z 
   intervalu (0-1000) na 5 míst s měnou 'Kč' tak, aby:
   a) čísla byla zarovnána vlevo     
   b) čísla byla zarovnána vpravo     
3) Načtěte z klávesnice řetězec, zjistěte jeho 
   délku a vypište jeho posledních 5 znaků   
"""

"""
Zkratky typů:
%i celé číslo
%f desetinné
%s řetězec
%x hexadecimální tvar
%o osmičkový tvar

"""



print u"Úkol 1"

x="%2i" % (20.14) 
print x
x="%5.5f" % (20.14)
print x
x="%s" % (20.14)
print x
x="%x" % (20.14)
print x
x="%o" % (20.14)
print x



print
print u"Úkol 2"

import random
for i in range(10):
    nahodne=random.randint(1,1000)
    y=u"%-5i Kč" % (nahodne)
    print y
    
print
import random
for i in range(10):
    nahodne=random.randint(1,1000)
    y=u"%5i Kč" % (nahodne)
    print y



print
print u"Úkol 2"

a=raw_input("Zadejte slovo: ")
print u"Posledních 5 písem: " ,a[-5:]

print u"Délka slova: ",len(a) ,u"písmen"





from pylab import *
x=arange(-10,10,0.2) # vektor x od - 10 do 10, krok 0.5

y1=2*x+1
y2=x**2
y3=x**4


grid (True) # mřížka
title("Graf bla bla")  # jméno
xlabel("Osa x")
ylabel("Osa y")
ylim(-5,40) #limity pro osu y
plot(x,y1, label="y1")  # vložení údajů
plot(x,y2, label="y2")
plot(x,y3, label="y3")

legend(("Prvni","Druha","Treti"),"lower right", shadow=True) #center , upper, lower, best
show() # zobrazení grafu




