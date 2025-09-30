set1_input = input("Введите числа для первого набора (через пробел): ")
set2_input = input("Введите числа для второго набора (через пробел): ")

set1 = set(map(float, set1_input.split()))
set2 = set(map(float, set2_input.split()))

common_numbers = set1 & set2

unique_numbers = set1 ^ set2

all_except_common = (set1 | set2) - common_numbers

print("Числа, которые присутствуют в обоих наборах:", common_numbers)
print("Числа, которые есть только в одном из наборов:", unique_numbers)
print("Числа из обоих наборов, за исключением общих:", all_except_common)
