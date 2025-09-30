def type_check(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {arg} is not of type {expected_type}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

try:
    print(add(2, 3))  
    print(add(2, "3"))  
except TypeError as e:
    print(e) 
