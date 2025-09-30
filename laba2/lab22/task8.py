import time

def timing(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = (end_time - start_time) * 1000

        print(f"Время выполнения функции {func.__name__}: {execution_time:.4f} миллисекунд")
        
        return result
    
    return wrapper

@timing
def slow_function():
    time.sleep(2) 

slow_function()
