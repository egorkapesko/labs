amount = int(input("Введите вашу сумму в рублях: "))

num_100 = amount // 100
amount %= 100

num_50 = amount // 50
amount %= 50

num_10 = amount // 10
amount %= 10

num_5 = amount // 5
amount %= 5

num_2 = amount // 2
amount %= 2

num_1 = amount  

print("Купюр по 100: " + str(num_100))
print("Купюр по 50: " + str(num_50))
print("Купюр по 10: " + str(num_10))
print("Купюр по 5: " + str(num_5))
print("Монет по 2: " + str(num_2))
print("Монет по 1: " + str(num_1))
