# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:14:53 2013


"""

ret=raw_input("Zadej retezec: ")

bez=""
for i in ret:
    if i==" ":
        bez+=""
    else:
        bez+=i

print bez
