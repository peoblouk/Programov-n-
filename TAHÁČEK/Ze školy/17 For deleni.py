# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:59:14 2012


"""

vstup=input(u"Zadejte číslo: ")
pocet=0

while (vstup<>0):
    for i in range (1,vstup+1):
        if vstup%i==0:
            pocet+=1

if pocet==2:
    print u"Prvočíslo."
else:
    print u"Není prvočíslo."
    
    print ""
    vstup=input(u"Další čáslo: ")
print "Koneeec"