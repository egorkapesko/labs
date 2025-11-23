import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA')
df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])
df['days_to_flight'] = (df['FLIGHT_DATE_LOC'] - df['ISSUE_DATE']).dt.days

print("1. ОБЩИЕ СТАТИСТИКИ")
print(f"Период: {df['ISSUE_DATE'].min().date()} - {df['ISSUE_DATE'].max().date()}")
print(f"Записей: {len(df)}")
print(f"Выручка: {df['REVENUE_AMOUNT'].sum()} руб.")
print(f"Средний чек: {df['REVENUE_AMOUNT'].mean():.0f} руб.")
print(f"Медиана: {df['REVENUE_AMOUNT'].median():.0f} руб.")

print("\n2. АЭРОПОРТЫ")
top_airports = pd.concat([df['ORIG_CITY_CODE'], df['DEST_CITY_CODE']]).value_counts().head(10)
print("Топ-10 аэропортов:")
print(top_airports)

print("\n3. СЕЗОННОСТЬ")
df['issue_month'] = df['ISSUE_DATE'].dt.month
monthly_analysis = df.groupby('issue_month').agg({
    'REVENUE_AMOUNT': ['sum', 'mean', 'count'],
    'days_to_flight': 'mean'
}).round(0)
print("Метрики по месяцам:")
print(monthly_analysis)

print("\n4. ПАССАЖИРЫ")
pax_analysis = df.groupby('PAX_TYPE').agg({
    'REVENUE_AMOUNT': ['mean', 'count', 'sum'],
    'days_to_flight': 'mean'
}).round(0)
print("Анализ по типам пассажиров:")
print(pax_analysis)

if 'FFP_FLAG' in df.columns:
    ffp_analysis = df.groupby('FFP_FLAG').agg({
        'REVENUE_AMOUNT': ['mean', 'count'],
        'days_to_flight': 'mean'
    }).round(0)
    print("Анализ по программе лояльности:")
    print(ffp_analysis)

print("\n5. СПОСОБЫ ОПЛАТЫ")
fop_analysis = df.groupby('FOP_TYPE_CODE').agg({
    'REVENUE_AMOUNT': ['mean', 'count', 'sum']
}).round(0)
print("Топ-5 способов оплаты:")
print(fop_analysis.head(5))

print("\n6. ПРОГНОЗИРОВАНИЕ")
monthly_sales = df.groupby(df['ISSUE_DATE'].dt.to_period('M')).size()
print("Продажи по месяцам:")
print(monthly_sales.tail(6))

monthly_flights = df.groupby(df['FLIGHT_DATE_LOC'].dt.to_period('M')).size()
print("Перелеты по месяцам:")
print(monthly_flights.tail(6))

if len(monthly_sales) > 1:
    avg_growth = monthly_sales.pct_change().mean()
    last_sales = monthly_sales.iloc[-1]
    forecast_sales = last_sales * (1 + avg_growth)
    print(f"Прогноз продаж: {forecast_sales:.0f} билетов")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

axes[0,0].hist(df['REVENUE_AMOUNT'], bins=30)
axes[0,0].set_title('Суммы продаж')

top_airports.head(8).plot(kind='bar', ax=axes[0,1])
axes[0,1].set_title('Топ аэропорты')

monthly_sales.plot(kind='line', marker='o', ax=axes[0,2])
axes[0,2].set_title('Продажи по месяцам')

pax_revenue = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].mean()
pax_revenue.plot(kind='bar', ax=axes[1,0])
axes[1,0].set_title('Средний чек по пассажирам')

df['FOP_TYPE_CODE'].value_counts().head(8).plot(kind='bar', ax=axes[1,1])
axes[1,1].set_title('Способы оплаты')

if len(monthly_sales) > 1:
    monthly_sales.plot(kind='line', ax=axes[1,2])
    axes[1,2].set_title('Тренд продаж')

plt.tight_layout()
plt.show()

print("\nВЫВОДЫ")
print(f"1. Всего продаж: {len(df)} на сумму {df['REVENUE_AMOUNT'].sum()} руб.")
print(f"2. Основные аэропорты: {top_airports.head(3).index.tolist()}")
print(f"3. Сезонность влияет на продажи и выручку")
print(f"4. Основной тип пассажиров: {df['PAX_TYPE'].value_counts().index[0]}")
print(f"5. Основные способы оплаты: {df['FOP_TYPE_CODE'].value_counts().head(3).index.tolist()}")
print(f"6. Прогноз: {'есть' if len(monthly_sales) > 1 else 'нет данных'}")