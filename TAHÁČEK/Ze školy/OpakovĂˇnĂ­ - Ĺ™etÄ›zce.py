# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:13:49 2013


"""

"""
Opakování - řetězce:
    
1) Načtěte řetězec a setřiďte v něm písmena podle abecedy.

"""

ret=raw_input("Zadejte slovo (EN) : ")

sez=[]
for i in ret:
    sez.append(i)

sez.sort()
ret=""
for i in sez:
    ret+=i

print ret