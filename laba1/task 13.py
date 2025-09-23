import random

random_number = random.randint(1, 100)

while True:
    num = int(input("Ведите число: "))
    if num > random_number:
        print("Больше")
    elif num < random_number:
        print("Меньше")
    else:
        print("Число разгадано")
        break