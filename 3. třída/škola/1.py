import math as m

print("Tento program vám vypočítá objem a povrch koule")
print("-----------------------------------------------")

polomer = int(input("Zadejte hodnotu poloměru: "))

objem = (4/3 * m.pi * polomer ** 3)
povrch = (4 * m.pi * polomer ** 2)

print(f"objem koule je V= {objem}")
print(f"povrch koule je S= {povrch}")
