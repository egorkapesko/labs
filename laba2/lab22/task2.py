def merge_dicts(dict_a, dict_b):
    for key in dict_b:
        if key in dict_a:
            if isinstance(dict_a[key], dict) and isinstance(dict_b[key], dict):
                merge_dicts(dict_a[key], dict_b[key])
            else:
                dict_a[key] = dict_b[key]
        else:
            dict_a[key] = dict_b[key]

def input_dict(prompt):
    dict_str = input(prompt)

    try:
        result = eval(dict_str)
        if not isinstance(result, dict):
            raise ValueError("Введенная строка не является словарем.")
        return result
    except Exception as e:
        print(f"Ошибка при вводе: {e}")
        return {}

dict_a = input_dict("Введите первый словарь: ")
dict_b = input_dict("Введите второй словарь: ")

merge_dicts(dict_a, dict_b)

print("Результат слияния:")
print(dict_a)
