str = input("Введите число: ")

num = int(str)

if num % 7 == 0:
    print("Магическое число!")

else:
    summa = sum(map(int, str))
    print("Сумма цифр:", summa)