familiya = input("Введите фамилию: ")
imya = input("Введите имя: ")
otchestvo = input("Введите отчество: ")

pervaya_bukva_imya = imya[0]

pervaya_bukva_otchestvo = otchestvo[0]

fio = familiya + " " + pervaya_bukva_imya + ". " + pervaya_bukva_otchestvo + "."

print("Форматированное ФИО:", fio)