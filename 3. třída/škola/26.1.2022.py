from cgi import test
import random as r

"""

colors = ["Red", "Black", "Green"]
# váhy určují šanci na to že padne daná barva
result = r.choices(colors, weights=[18, 18, 2], k=10)

print(result)
x

for i in range(20):
    print(r.normalvariate(0, 1))
print()
for i in range(20):
    print(r.normalvariate(0, 1))
print()
for i in range(20):
    print(r.normalvariate(5, 0.2))
"""

hodnoty = list(range(1, 53))

print(hodnoty)
print()

"""
r.shuffle(hodnoty)
print(hodnoty)
"""

def poradi():
    tes = r.shuffle(hodnoty)
    return tes
poradi()


print(tes)

"""
vyber = r.sample(hodnoty, k = 5)
print(vyber)
"""