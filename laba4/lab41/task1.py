import matplotlib.pyplot as plt
import numpy as np
import math

def task1():
    x_degrees = np.linspace(-360, 360, 1000)
    x_radians = np.radians(x_degrees)
    
    f_x = np.exp(np.cos(x_radians)) + np.log(np.cos(0.6*x_radians)**2 + 1) * np.sin(x_radians)
    h_x = -np.log((np.cos(x_radians) + np.sin(x_radians))**2 + 2.5) + 10
    
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(x_degrees, f_x, 'b-', linewidth=2)
    plt.title('Функция f(x)')
    plt.xlabel('Градусы')
    plt.ylabel('f(x)')
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(x_degrees, h_x, 'r-', linewidth=2)
    plt.title('Функция h(x)')
    plt.xlabel('Градусы')
    plt.ylabel('h(x)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    task1()