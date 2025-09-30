base_minutes = 60 
base_sms = 30  
base_traffic_mb = 1024  
base_price = 24.99  

extra_minute_cost = 0.89  
extra_sms_cost = 0.59  
extra_traffic_cost = 0.79  

tax_rate = 0.02  

used_minutes = int(input("Введите количество использованных минут за месяц: "))
used_sms = int(input("Введите количество использованных смс за месяц: "))
used_traffic = float(input("Введите количество использованного интернет-трафика в Мб: "))

total_amount = base_price

extra_minutes_cost = 0
extra_sms_cost_total = 0
extra_traffic_cost_total = 0

if used_minutes > base_minutes:
    extra_minutes = used_minutes - base_minutes
    extra_minutes_cost = extra_minutes * extra_minute_cost
    total_amount += extra_minutes_cost

if used_sms > base_sms:
    extra_sms = used_sms - base_sms
    extra_sms_cost_total = extra_sms * extra_sms_cost
    total_amount += extra_sms_cost_total

if used_traffic > base_traffic_mb:
    extra_traffic = used_traffic - base_traffic_mb
    extra_traffic_cost_total = extra_traffic * extra_traffic_cost
    total_amount += extra_traffic_cost_total

tax_amount = total_amount * tax_rate
total_amount_with_tax = total_amount + tax_amount

print(f"\nФиксированная сумма тарифа: {base_price:.2f} руб.")

if extra_minutes_cost > 0:
    print(f"Стоимость дополнительных минут: {extra_minutes_cost:.2f} руб. (Тариф превышен на {extra_minutes} минут)")

if extra_sms_cost_total > 0:
    print(f"Стоимость дополнительных смс: {extra_sms_cost_total:.2f} руб. (Тариф превышен на {extra_sms} смс)")

if extra_traffic_cost_total > 0:
    print(f"Стоимость дополнительного интернет-трафика: {extra_traffic_cost_total:.2f} руб. (Тариф превышен на {used_traffic - base_traffic_mb:.2f} Мб)")

print(f"Сумма налога (2%): {tax_amount:.2f} руб.")
print(f"Итоговая сумма к оплате: {total_amount_with_tax:.2f} руб.")