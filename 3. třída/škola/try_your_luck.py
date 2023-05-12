import numbers
import random as r
import time as t

# variable
wait = 0.7  # can be change if you don't want to wait
number = r.randint(0, 10)  # can be change to larger range

# colors
green = "\033[92m"
orange = "\033[93m"
end = "\033[0m"


# welcome
print(f"{orange}Computer: This program will try your luck{end}")
print(f"{orange}Computer: Don't let the computer win!{end}")
t.sleep(wait)
print(f"{orange}Computer: Try to hit number from 0 to 10{end}")
print(f"{orange}Computer: you always get some tip{end}")
chance = int(input(f"{orange}Computer: put number of chances > {end}"))
t.sleep(wait)


while True:
    if chance == 0:
        print(f"{orange}Computer: End of the game! Number was {number}{end}")
        t.sleep(wait)
        break

    # test your input
    try:
        user = int(input(f"{green}User: number > {end}"))
        t.sleep(wait)
        if number >= 11:
            raise ValueError

    except ValueError:
        print(f"{orange}Computer: Wrong input!{end}")
        chance = chance - 1
        print(f"{orange}Computer: you have {chance}{end}")

    # hit number
    if user == number:
        t.sleep(wait)
        print(f"{orange}Computer: amazing, you hit that number!{end}")
        exit()

    # number is smaller
    elif user > number:
        t.sleep(wait)
        print(f"{orange}Computer: number is smaller than i think{end}")
        print("")
        chance = chance - 1
        print(f"{orange}Computer: you have {chance}{end}")

    # number is higher
    elif user < number:
        t.sleep(wait)
        print(f"{orange}Computer: number is higher than i think{end}")
        print("")
        chance = chance - 1
        print(f"{orange}Computer: you have {chance}{end}")

print("")
print(f"{green}Computer: I'm winner!{end}")
