Day = int(input("Введите день: "))
Month = int(input("Введите номер месяца (1-12): "))

if (Month == 1 and Day >= 20) or (Month == 2 and Day <= 18):
    print("Водолей")
elif (Month == 2 and Day >= 19) or (Month == 3 and Day <= 20):
    print("Рыбы")
elif (Month == 3 and Day >= 21) or (Month == 4 and Day <= 19):
    print("Овен")
elif (Month == 4 and Day >= 20) or (Month == 5 and Day <= 20):
    print("Телец")
elif (Month == 5 and Day >= 21) or (Month == 6 and Day <= 20):
    print("Близнецы")
elif (Month == 6 and Day >= 21) or (Month == 7 and Day <= 22):
    print("Рак")
elif (Month == 7 and Day >= 23) or (Month == 8 and Day <= 22):
    print("Лев")
elif (Month == 8 and Day >= 23) or (Month == 9 and Day <= 22):
    print("Дева")
elif (Month == 9 and Day >= 23) or (Month == 10 and Day <= 22):
    print("Весы")
elif (Month == 10 and Day >= 23) or (Month == 11 and Day <= 21):
    print("Скорпион")
elif (Month == 11 and Day >= 22) or (Month == 12 and Day <= 21):
    print("Стрелец")
elif (Month == 12 and Day >= 22) or (Month == 1 and Day <= 19):
    print("Козерог")
else:
    print("Введена неверная дата")
