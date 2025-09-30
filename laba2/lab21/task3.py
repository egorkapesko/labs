numbers = input("Введите числа через пробел: ")

num_list = numbers.split()

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

num_list.sort()

print("Отсортированные числа:", num_list)

if len(num_list) >= 2:
    second_largest = num_list[-2]
    print("Второе по величине число:", second_largest)
else:
    print("Нужно ввести хотя бы два числа!")