# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:06:38 2012


"""

from Tkinter import * 

"""
hlavni = Tk()
v = IntVar() 

c = Checkbutton(hlavni, text="Přepínač", variable=v) 
c.grid(row=0,column=1) 

def tisk():
    if v.get()==0:
        print "Off"
    else:
        print "On"   
    
tlacitko=Button(hlavni,text="Kontrola",command=tisk)
tlacitko.grid(row=0,column=0)
 
mainloop() 

"""



#####################  ÚKOL ########################

"""

1) Vložte do okna 2 zaškrtávací políčka a 1 tlačítko inverze, 
   které prohodí u obou políček "On" / "Off"
   
"""

hlavni = Tk()

b = IntVar()
c = IntVar() 
 
a1 = Checkbutton(hlavni, text="Přepínač", variable=b) 
a1.grid(row=0,column=1) 

a2 = Checkbutton(hlavni, text="Přepínač", variable=c) 
a2.grid(row=0,column=2) 

def Prohodit():
    b.set((b.get()+1)%2)
    c.set((c.get()+1)%2)

tlacitko=Button(hlavni,text="Prohodit",command=Prohodit)
tlacitko.grid(row=0,column=0)
 
hlavni.mainloop()

