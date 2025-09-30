def cache(func):
    cached_results = {}
    
    def wrapper(*args):
        if args in cached_results:
            print(f"Результат для {args} взят из кэша.")
            return cached_results[args]
        else:
            result = func(*args)
            cached_results[args] = result
            print(f"Результат для {args} сохранен в кэш.")
            return result
    return wrapper

@cache
def square(x):
    return x * x

while True:
    try:
        user_input = input("Введите число для вычисления его квадрата (или 'exit' для выхода): ")
        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break

        number = float(user_input)

        result = square(number)

        print(f"Квадрат числа {number} равен {result}.")
    except ValueError:
        print("Пожалуйста, введите корректное число или 'exit' для выхода.")
