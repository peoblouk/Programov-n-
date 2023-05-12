# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:21:47 2013


"""
"""

from Tkinter import *
from tkFileDialog import *

hlavni=Tk()

def Otevrit():
    ret = askopenfilename(title=u"Otevřít soubor")
    print ret
    #otevření pro čtení, čtení a uzavření
    
def Ulozit():
    ret = asksaveasfilename(title=u"Uložit soubor", initialdir="c:")
    print ret
    #otevření pro zápis, zápis a uzavření



button1=Button(hlavni,text=u"Otevřít",command=Otevrit)
button1.pack(pady=3) 
button2=Button(hlavni,text=u"Uložit",command=Ulozit)
button2.pack(pady=3) 
mainloop()
"""
"""
Úkol:
1) Načtěte název textového souboru pomocí fce 
   asksaveasfilename a zapište do něj 100 náhodných 
   barev v hexa kódu pod sebou.
"""   



from Tkinter import *
from tkFileDialog import *
import random as r

hlavni=Tk()

   
def Ulozit():
    s = asksaveasfilename(title=u"Uložit soubor")
    soubor=open(s,"w")
    for i in range(100):
        soubor.write("#%02x%02x%02x\n" %(r.randint(0,255), r.randint(0,255), r.randint(0,255)))   
    soubor.close()

button1=Button(hlavni,text=u"Save",command=Ulozit)
button1.pack(pady=3) 
mainloop()




