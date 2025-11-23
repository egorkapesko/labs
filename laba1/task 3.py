password = input("Введите пароль: ")

if len(password) < 16:
    print("Слишком короткий")
else:

    if password.isalpha():  
        print("Слабый пароль (используйте цифры)")

    elif password.isdigit():
        print("Слабый пароль (используйте буквы)")
    else:
        print("Надежный пароль")я
