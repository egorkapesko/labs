import numpy as np

def transport_expenses():
    expenses = np.array([120, 110, 115, 100, 90, 85, 80, 85, 95, 105, 115, 125])
    
    winter = expenses[0:2].sum() + expenses[11]  
    summer = expenses[5:8].sum()  
    
    print(f"Зимние расходы: {winter}")
    print(f"Летние расходы: {summer}")
    
    if winter > summer:
        print("Зимой тратится больше денег на проезд")
    else:
        print("Летом тратится больше денег на проезд")
    
    max_expense = expenses.max()
    max_months = np.where(expenses == max_expense)[0] + 1
    print(f"Наибольшие расходы в месяцах: {max_months.tolist()}")
    
    return expenses

if __name__ == "__main__":
    print("Задача 1: Расходы на проезд")
    transport_expenses()