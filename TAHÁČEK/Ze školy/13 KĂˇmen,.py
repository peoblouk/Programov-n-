# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 09:08:01 2012


"""

import random

volba=input(u"Vyberte: (Kámen=1, Nůžky=2, Papír=3): ")

if volba==1:
    print (u"Vaše volba je: Kámen")   
elif volba==2:
    print (u"Vaše volba je: Nůžky")
elif volba==3:
    print (u"Vaše volba je: Papír")
else:
    print (u"Špatná hodnota")

PC=random.randint(1,3)

if PC==1:
    print (u"Volba PC je: Kámen")   
elif PC==2:
    print (u"Volba PC je: Nůžky")
else:
    print (u"Volba PC je: Papír")


if volba==PC:
    print (u"Remíza!")
if (volba==1 and PC==2) or (volba==2 and PC==3) or (volba==3 and PC==1):
    print (u"Jsi vítěz!")    
if (volba==1 and PC==3) or (volba==2 and PC==1) or (volba==3 and PC==2):
    print (u"Prohrál jsi!")