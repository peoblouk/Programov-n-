from random import randint

def control(limit):
    try:
        limit = int(input("enter limit of generated number: "))
        if limit <= 0:
            raise ValueError
    except ValueError:
        print("number must be > 0")

control()
randint(0, 
