import matplotlib.pyplot as plt
import numpy as np

def task2():
    x = np.linspace(-10, 10, 1000)
    y = (x**2 - 9) / (x**2 + 1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'g-', linewidth=2)
    plt.title('График функции f(x) = (x² - 9)/(x² + 1)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.show()

if __name__ == "__main__":
    task2()