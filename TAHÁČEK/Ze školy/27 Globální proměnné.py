# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:19:13 2014


"""
"""
Globální a lokální proměnné
- proměnné definované uvnitř funkcí, jsou tzv. lokální = po skončení
  funkce přestanou existovat
- global x = definice globální proměnné x (existuje po celou dobu 
  trvání programu)   
- pokud chceme uvnitř funkce zapisovat do globální proměnné,
  musíme před ni napsat také global
"""

 
def funkce1():
    x=10      #vznik lokální proměnné
    print x   #tisk lok. proměnné 

#funkce1()
#print x   #pokus o tisk lok. proměnné, která neexistuje
   

z=1       #vznik globální proměnné z
def funkce2():
    z=10      #vznik lokální proměnné z!!!!!!
    print z   #tisk lok. proměnné 

#funkce2()
#print z   #tisk globální proměnné

y=1
def funkce3():
    global y  #vznik globální proměnné y uvnitř funkce,
    print y
    y=100     #pokud již existovala, budeme pracovat s ní
    
funkce3() #proměnná y bude existovat až po volání funkce3
print y   #tisk globální proměnné y

"""
Úkol:
1) Napište program pro obsluhu účtu. Bude mít 2 funkce:
   Vklad(x) - přidá peníze na účet
   Vyber(x) - odebere peníze z účtu
   S účtem budou pracovat jako s globální proměnnou.
"""