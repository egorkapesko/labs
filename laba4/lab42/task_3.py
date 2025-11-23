import numpy as np

def solve_linear_system():
    
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]])
    
    B = np.array([8, -11, -3])
    
    try:
        A_inv = np.linalg.inv(A)
        X = np.dot(A_inv, B)
        print("Решение системы уравнений:")
        print(f"x = {X[0]:.1f}, y = {X[1]:.1f}, z = {X[2]:.1f}")

        check = np.dot(A, X)
        print("Проверка:")
        print(f"2*{X[0]:.1f} + {X[1]:.1f} - {X[2]:.1f} = {check[0]:.1f} (должно быть 8)")
        print(f"-3*{X[0]:.1f} - {X[1]:.1f} + 2*{X[2]:.1f} = {check[1]:.1f} (должно быть -11)")
        print(f"-2*{X[0]:.1f} + {X[1]:.1f} + 2*{X[2]:.1f} = {check[2]:.1f} (должно быть -3)")
        
        return X
    except np.linalg.LinAlgError:
        print("Матрица вырождена")
        return None

if __name__ == "__main__":
    print("Задача 3: Система линейных уравнений")
    solve_linear_system()