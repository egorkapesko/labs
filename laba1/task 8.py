string = input("Введите вашу строку: ")
length = len(string)

if length % 2 == 0:
    first_half = string[0:(length // 2)]
    second_half = string[(length // 2):length]
    second_half_reverse = ''.join(reversed(second_half))
    print("Количество символов в строке четно")
    if first_half == second_half_reverse:
        print("Строка является палиндромом")
    else:
        print("Строка не является палиндромом")
else:
    first_half = string[0:(length // 2)]
    second_half = string[(length // 2 + 1):length]
    second_half_reverse = ''.join(reversed(second_half))
    print("Количество символов в строке нечетно")
    if first_half == second_half_reverse:
        print("Строка является палиндромом")
    else:
        print("Строка не является палиндромом")
