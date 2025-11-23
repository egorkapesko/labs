import numpy as np

def car_travel():
    lengths = np.array([20, 8, 9, 18, 5, 12, 16, 16, 6, 7])
    speeds = np.array([44, 70, 44, 66, 46, 38, 38, 37, 66, 67])
    
    k = 4  
    p = 7 

    route_lengths = lengths[k-1:p]
    route_speeds = speeds[k-1:p]
    
    total_length = route_lengths.sum()

    times = route_lengths / route_speeds
    total_time = times.sum()
    
    average_speed = total_length / total_time
    
    print(f"S = {total_length:.0f} км")
    print(f"T = {total_time:.2f} час")
    print(f"V = {average_speed:.2f} км/ч")
    
    return total_length, total_time, average_speed

if __name__ == "__main__":
    print("Задача 2: Расчет пути автомобиля")
    car_travel()