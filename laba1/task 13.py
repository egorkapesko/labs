import random

num = random.randint(1,100)
print("Вам нужно отгадать число от 1 до 100\n")

v_num = int(input("Введите ваше число от 1 до 100: "))
while v_num != num:
    if v_num > num:
        print("Загаданное число меньше вашего\n")
    else:
        print("Загаданное число больше вашего\n")
    v_num = int(input("Введите новое число от 1 до 100: "))

print("Вы отгадали число")