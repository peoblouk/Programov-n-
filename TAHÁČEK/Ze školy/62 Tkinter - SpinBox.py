# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 11:49:29 2013


"""

from Tkinter import *

hlavni = Tk()
hodnota=StringVar()
hodnota.set("0")

def Nastav():
    l["text"]=str(w.get())
    
w = Spinbox(hlavni, from_=-50, to=1000,textvariable=hodnota,command=Nastav)
w.pack()
l=Label(hlavni,text="0",font="Arial 20")
l.pack()

mainloop()