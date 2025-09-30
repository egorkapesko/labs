numbers_input = input("Введите список чисел (через пробел): ")

numbers = numbers_input.split() 
numbers = [float(num) for num in numbers]  

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

repeated_numbers = []
for num in unique_numbers:
    if numbers.count(num) > 1 and num not in repeated_numbers:
        repeated_numbers.append(num)

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

negative_numbers = []
for num in numbers:
    if num < 0:
        negative_numbers.append(num)

float_numbers = []
for num in numbers:
    if isinstance(num, float):
        float_numbers.append(num)

sum_multiples_of_5 = 0
for num in numbers:
    if num % 5 == 0:
        sum_multiples_of_5 += num

max_number = numbers[0]
min_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num

def format_number(num):
    if num.is_integer():  
        return int(num)  
    return num  

print("Уникальные числа:", [format_number(num) for num in unique_numbers])
print("Повторяющиеся числа:", [format_number(num) for num in repeated_numbers])
print("Четные числа:", [format_number(num) for num in even_numbers])
print("Нечетные числа:", [format_number(num) for num in odd_numbers])
print("Отрицательные числа:", [format_number(num) for num in negative_numbers])
print("Числа с плавающей точкой:", [format_number(num) for num in float_numbers])
print("Сумма чисел, кратных 5:", sum_multiples_of_5)
print("Самое большое число:", format_number(max_number))
print("Самое маленькое число:", format_number(min_number))
