# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:09:08 2013


"""

vstup=open('vstup.txt','r')
vystup=open('vystup.txt','w')
radek=vstup.readline()
ret="%s" %(radek)
print ret



vstup.seek(1,0)
pismeno=(vstup.read(1))
vystup.write(pismeno)


vstup.seek(0,0)
pismeno2=(vstup.read(1))
vystup.write(pismeno2)



vstup.seek(3,0)
pismeno3=(vstup.read(1))
vystup.write(pismeno3)



vstup.seek(2,0)
pismeno4=(vstup.read(1))
vystup.write(pismeno4)


vstup.seek(5,0)
pismeno5=(vstup.read(1))
vystup.write(pismeno5)


vstup.seek(4,0)
pismeno6=(vstup.read(1))
vystup.write(pismeno6)


vstup.seek(7,0)
pismeno7=(vstup.read(1))
vystup.write(pismeno7)



vstup.seek(6,0)
pismeno8=(vstup.read(1))
vystup.write(pismeno8)


vstup.seek(9,0)
pismeno9=(vstup.read(1))
vystup.write(pismeno9)


vstup.seek(8,0)
pismeno10=(vstup.read(1))
vystup.write(pismeno10)

