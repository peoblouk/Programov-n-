# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:17:13 2013


"""

from Tkinter import *

hlavni = Tk()

w = Label(hlavni, text=u"Červená", bg="red", fg="white")
w.pack(fill=Y, expand=1)
w = Label(hlavni, text=u"Zelená", bg="green", fg="black")
w.pack(fill=X)
w = Label(hlavni, text=u"Modrá", bg="blue", fg="white")
w.pack(fill=BOTH, expand=1)

mainloop()