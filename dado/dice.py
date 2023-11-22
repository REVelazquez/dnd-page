import random
def dice(input):
    if input == 6:
        return random.randint(1, 6)
    elif input ==8:
        return random.randint(1, 8)
    elif input ==10:
        return random.randint(1, 10)
    elif input ==20:
        return random.randint(1, 20)
    elif input ==100:
        return random.randint(1, 100)
    