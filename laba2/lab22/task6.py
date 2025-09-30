def unique_elements(lst, unique_set=None):
    if unique_set is None:
        unique_set = set()

    for element in lst:
        if isinstance(element, list):
            unique_elements(element, unique_set)
        else:
            unique_set.add(element)

    return list(unique_set) 

input_string = input("Введите вложенный список (например, [1, 2, [3, 4], [5, 6]]): ")

try:
    user_list = eval(input_string)
    if isinstance(user_list, list):
        result = unique_elements(user_list)
        print("Уникальные элементы:", result)
    else:
        print("Введённые данные не являются списком!")
except:
    print("Ошибка ввода! Убедитесь, что вы ввели корректный вложенный список.")
