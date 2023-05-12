# -*- coding: utf-8 -*-
"""
Created on Tue Apr 02 12:04:24 2013


"""

from Tkinter import *

hlavni = Tk()

w = Canvas(hlavni,width=200, height=100)
w.pack()

def ZmenaCary(udalost):
    w.itemconfig(obdelnik,fill="green")
  
elipsa=w.create_oval(0,0,50,50,fill="green")  
cara1=w.create_line(0, 0, 200, 100,fill="yellow")
cara2=w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
obdelnik=w.create_rectangle(50, 25, 150, 75, fill="blue")

print elipsa, cara1, cara2, obdelnik

w.bind("<1>",ZmenaCary)

mainloop()

"""
Úkol:
1)Nakreslete 5 úseček s náhodnými souřadnicemi.
  Pomocí cyklu!
""" 