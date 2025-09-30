import time
from functools import wraps

def log_calls(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            call_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

            func_name = func.__name__

            with open(filename, 'a') as f:
                f.write(f"[{call_time}] {func_name} called with arguments {args} and keyword arguments {kwargs}\n")

            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

@log_calls("logfile.txt")
def add(a, b):
    return a + b

@log_calls("logfile.txt")
def multiply(a, b, c):
    return a * b * c

def main():
    print("Введите два числа для сложения (через пробел):")
    a, b = map(int, input().split())
    print("Введите три числа для умножения (через пробел):")
    x, y, z = map(int, input().split())

    result_add = add(a, b)
    result_multiply = multiply(x, y, z)

    print(f"Результат сложения: {result_add}")
    print(f"Результат умножения: {result_multiply}")
    print("\nИнформация о вызовах записана в файл 'logfile.txt'.")

if __name__ == "__main__":
    main()
