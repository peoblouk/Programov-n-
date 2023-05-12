# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:24:22 2012


"""

from Tkinter import *

"""

okno = Tk()

promenna = StringVar()
promenna.set(u"Jedna") # standardní hodnota

def test(hodnota):
    if hodnota=="dva":
        print "Byla to dvojka"
    else:
        print "Nebyla to dvojka"
    print u"Výsledek je", hodnota    

w = OptionMenu(okno, promenna, u"jedna", u"dva", u"tři","mrkev",u"čtyři",command=test)
w.pack(side="left")

#tlacitko=Button(okno,text="Testuj dvojku",command=test)
#tlacitko.pack(side="left")

mainloop()

"""


"""

1) Vytvořte rozbalovací nabídku s třemi barvami a při výběru
   nastavte danou barvu na pozadí okna
   
"""


okno = Tk()

promenna = StringVar()
promenna.set(u"Základní") # standardní hodnota

def barva(hodnota):
    if hodnota==u"zelená":
        okno["bg"]="green"
    if hodnota==u"modrá":
        okno["bg"]="blue"
    if hodnota==u"červená":
        okno["bg"]="red"
 

w = OptionMenu(okno, promenna, u"zelená", u"modrá", u"červená", command=barva)
w.pack(side="left")

mainloop()
