# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:35:00 2013


"""

from Tkinter import *
from tkColorChooser import *

hlavni=Tk()

barva=askcolor(title="Barva")
print barva
print barva[0][1]
print barva[1]
hlavni["bg"]=barva[1]


mainloop()