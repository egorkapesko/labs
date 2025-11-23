import numpy as np

def calculate_integrals():
    def f1(x):
        return x**2 + 2*x + 1

    def trapezia_method(f, a, b, n=1000):
        h = (b - a) / n
        result = 0.5 * (f(a) + f(b))
        for i in range(1, n):
            result += f(a + i * h)
        return result * h

    def double_integral(f, x1, x2, y1, y2, n=100):
        dx = (x2 - x1) / n
        dy = (y2 - y1) / n
        result = 0
        
        for i in range(n):
            x = x1 + (i + 0.5) * dx
            for j in range(n):
                y = y1 + (j + 0.5) * dy
                result += f(x, y)
        
        return result * dx * dy

    result1 = trapezia_method(f1, 0, 2)
    print(f"∫(x² + 2x + 1)dx от 0 до 2 = {result1:.3f}")

    def f2(x, y):
        return x + y
    
    result2 = double_integral(f2, 0, 1, 0, 1)
    print(f"∫∫(x + y)dxdy = {result2:.3f}")

    analytical1 = (2**3/3 + 2**2 + 2) - (0)
    analytical2 = 1.0 
    
    print(f"Аналитическое решение первого интеграла: {analytical1:.3f}")
    print(f"Аналитическое решение второго интеграла: {analytical2:.3f}")
    
    return result1, result2

if __name__ == "__main__":
    calculate_integrals()