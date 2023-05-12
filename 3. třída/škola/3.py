import math as m

print("Tento program vám vypočítá kořeny kvadratické rovnice")
print("-----------------------------------------------------")
print("")
print("Tvar rovnice je ax² + bx + c")
a = int(input("Zadejte hodnotu proměnné a =  "))
b = int(input("Zadejte hodnotu proměnné b =  "))
c = int(input("Zadejte hodnotu proměnné c =  "))

D = [(b ** 2) - (4 * a * c)]
x1 = [(-b + m.sqrt(D)) / (2 * a)]
x2 = [(-b - m.sqrt(D)) / (2 * a)]

print(f"Kořeny rovnice jsou x₁= {x1} , x₂= {x2}")
