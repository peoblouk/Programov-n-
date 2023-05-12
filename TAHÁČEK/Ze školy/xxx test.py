# -*- coding: utf-8 -*-
"""
Created on Wed Apr 03 08:22:36 2013


"""


#SKUPINA A


ret=raw_input(u"Zadej řetězec: ")

pom=""
for i in ret:
    if i=="a":
        pom+="A"
    else:
        pom+=i
    pom+=" "

print pom


# SKUPINA B

ret=raw_input("Zadejte slovo: ")
novy=""
for i in ret:
    novy=i+novy
    
print novy