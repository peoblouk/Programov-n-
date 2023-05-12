# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:09:50 2013


"""

vstup=open("vstup.txt","r")
vystup=open("vystup.txt","w")

"""
radky=int(vstup.readlines)
for i in range(radky):
"""

for i in range(4):
    cislo=int(vstup.read(1))
    pismeno=(vstup.read(1))
    znaky=str(pismeno*cislo)
    vystup.write("%s\n" % znaky)
    vstup.seek(2,1)

vstup.close()
vystup.close()