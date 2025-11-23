ip_address = input("Введите IP-адрес: ")

parts = ip_address.split(".")

if len(parts) == 4:
    first, second, third, fourth = parts[0], parts[1], parts[2], parts[3]

    if first.isdigit() and second.isdigit() and third.isdigit() and fourth.isdigit():
        if 0 <= int(first) <= 255 and 0 <= int(second) <= 255 and 0 <= int(third) <= 255 and 0 <= int(fourth) <= 255:
            print("Это корректный IP-адрес.")
        else:
            print("Это некорректный IP-адрес.")
    else:
        print("Это некорректный IP-адрес.")
else:
    print("Это некорректный IP-адрес.")
