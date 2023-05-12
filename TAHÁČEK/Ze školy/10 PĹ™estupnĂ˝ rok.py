# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:56:14 2012


"""

rok=input ("Zadejte rok: ")
if rok%4==0 and (rok%400==0 or rok%100!=0):
    print u"Rok je přestupný"
else: 
    print u"Rok není přestupný"