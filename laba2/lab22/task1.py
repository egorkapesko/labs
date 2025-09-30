def flatten_list(input_list):
    i = 0
    while i < len(input_list):
        if isinstance(input_list[i], list):
            input_list[i:i+1] = input_list[i]
        else:
            i += 1

input_string = input("Введите список чисел и/или вложенных списков (например, [1, [2, 3], 4]): ")

try:
    input_list = eval(input_string)
    if not isinstance(input_list, list): 
        print("Ошибка: введённое не является списком.")
    else:
        print(f"Исходный список: {input_list}")
        flatten_list(input_list)  
        print(f"Плоский список: {input_list}")
except:
    print("Ошибка: введённая строка не является корректным списком.")
