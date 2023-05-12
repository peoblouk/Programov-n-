# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:05:50 2012


"""
import math

a=input("Zadejte hodnutu a: ")
b=input("Zadejte hodnutu b: ")
c=input("Zadejte hodnutu c: ")

D=(b^2)-(4*a*c)
print "Diskriminant je: ", D

if D<0:
    print u"Nemáš řešení"

if D==0:
    x=(-b)/2*a
    print u"Má 1 řešení: ", x

else:
    x1=((-b)+math.sqrt(D))/2*a
    x2=((-b)-math.sqrt(D))/2*a
    print u"Má 2 řešení: ", x1, x2
