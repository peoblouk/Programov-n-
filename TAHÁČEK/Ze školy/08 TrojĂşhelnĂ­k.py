# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:21:56 2012


"""

a=input("Zadejte stranu a: ")
b=input("Zadejte stranu b: ")
c=input("Zadejte stranu c: ")

if (a+b>c) and (a+c>b) and (b+c>a):
    print u"Trojúhelník lze sestrojit"
    if (c^2==a^2+b^2) or (b^2==a^2+c^2) or (a^2==c^2+b^2):
        print u"Trojúhelník je pravoúhlý"
    else: 
        print u"Trojúhelník není pravoúhlý"

else:
    print u"Trojúhelník nelze sestrojit"