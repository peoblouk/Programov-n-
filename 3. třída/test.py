import random

x = 0
soucet = 0
while True:
    try:
        password = input("password: ")
    
    expect:
        print("Error incorrect input")
        for letter in password:
        cislo = random.randint(1, 20)
        x = cislo
        chance = {letter: x}
        print(chance)

        for number in chance:
            soucet = chance.values()
            print(soucet)
