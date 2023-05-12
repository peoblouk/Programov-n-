# -*- coding: utf-8 -*-
"""
Řetězce (string)
- uzavřeny v apostrofech (') nebo v uvozovkách (")
- trojí uvozovky mohou uzavírat i více řádků

Speciální znaky - začínají lomítkem
\' - apostrof
\" - uvozovka
\\ - lomítko
\n - nový řádek

ret= r"Specialni \n znaky: \' \\ \" "
print ret
"""

"""
Formátovací operátor %
- slouží ke vkládání a formátování různých
  datových typů do řetězce
Obecně:
"...%zkratka typu ..." % (N-tice hodnot)  

Zkratky typů:
%i celé číslo
%f desetinné
%s řetězec
%x hexadecimální tvar
%o osmičkový tvar

%5.2f číslo bude složeno z 5 znaků, z toho 2
      budou za desetinnou tečkou, chybějící znaky
      budou nahrazeny mezerami zleva

%-8.2f číslo bude složeno z 8 znaků, z toho 2
      budou za desetinnou tečkou, chybějící znaky
      budou nahrazeny mezerami zprava

%4i  obdobně pro celá čísla 
%-4i
Indexování
K jednotlivým částem řetezce lze přistoupit 
pomocí [].
Kladné hodnoty číslují znaky zleva, záporné zprava.      

ret="patek"
print ret[-1]       # poseldní znak
"""

"""
Operátor : (slice)
- vrací podřetězec
[:n] - vrátí prvních n znaků
[n:] - vrátí podřetězec od pozice n do konce
[m:n] - vrátí podřetězec od pozice m do n
"""
#print ret[:3]
#print ret[-3:]
#print ret[1:3]
"""


Funkce str()
- převede libovolný typ na řetězec
"""
#sez=[1,3,8]
#ret=str(sez)
#print sez
#print ret

"""
z=24
x="Cele %4i desetinne %-8.2f text" % (z,z)
print x


w="Retezec %s retezec" % 'vlozeny text'
print w

y="Hexadecimalni %x oktalove %o" % (z,z)
print y

slovnik={'cislo':1000000,'text':'nejaky text'}
v="Slovnik %(text)s" % slovnik
print v
"""
"""
ret="Pokusny retezec"
print ret[4:10]
seznam=[3, 'three', 3.0]
ret="Cislo "+str(seznam)
print ret
"""

"""
Úkol:
1) Vypište číslo 20.14 pomocí všech možných typů (i,f,x,o,s)
2) Vypište pod sebe seznam 10 náh. čísel z 
   intervalu (0-1000) na 5 míst s měnou 'Kč' tak, aby:
   a) čísla byla zarovnána vlevo     
   b) čísla byla zarovnána vpravo     
3) Načtěte z klávesnice řetězec, zjistěte jeho 
   délku a vypište jeho posledních 5 znaků   
"""

"""
Zkratky typů:
%i celé číslo
%f desetinné
%s řetězec
%x hexadecimální tvar
%o osmičkový tvar

"""



print u"Úkol 1"

x="%2i" % (20.14) 
print x
x="%5.5f" % (20.14)
print x
x="%s" % (20.14)
print x
x="%x" % (20.14)
print x
x="%o" % (20.14)
print x



print
print u"Úkol 2"

import random
for i in range(10):
    nahodne=random.randint(1,1000)
    y=u"%-5i Kč" % (nahodne)
    print y
    
print
import random
for i in range(10):
    nahodne=random.randint(1,1000)
    y=u"%5i Kč" % (nahodne)
    print y



print
print u"Úkol 2"

a=raw_input("Zadejte slovo: ")
print u"Posledních 5 písem: " ,a[-5:]

print u"Délka slova: ",len(a) ,u"písmen"




























