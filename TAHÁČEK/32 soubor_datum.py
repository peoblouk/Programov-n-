# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 08:23:40 2013


"""

from dat import *

soubor=open("datum.txt","r")
datum=soubor.readline()
soubor.close()
print datum

if TestDatumu(datum)==True:
    print "Datum OK"
else:
    print "Datum ERROR"    