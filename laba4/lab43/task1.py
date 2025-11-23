import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random
from datetime import datetime

fake = Faker('ru_RU')  # Используем русскую локаль, она подходит для Беларуси

def generate_belarusian_phone():
    """Генерирует белорусский номер телефона"""
    operators = ['29', '33', '44', '25']  # коды белорусских операторов
    operator = random.choice(operators)
    number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f"+375{operator}{number}"

def generate_student_data(num_students=1000):
    data = []
    subjects = ['Математика', 'Физика', 'Химия', 'Биология', 'История', 'Русский язык']
    specialties = ['Программирование', 'Математика', 'Физика', 'Химия', 'Биология', 'История']  
    study_forms = ['Бюджет', 'Платная', 'Целевая']
    
    # Белорусские города
    belarusian_cities = ['Минск', 'Гомель', 'Могилев', 'Витебск', 'Гродно', 'Брест', 'Барановичи', 'Борисов', 'Пинск', 'Орша']
    
    for _ in range(num_students):
        year = random.randint(2020, 2025)
        fio = fake.name()
        study_form = random.choice(study_forms)
        subject_scores = {subject: random.randint(1, 100) for subject in subjects}
        avg_certificate = round(random.uniform(4.0, 10.0), 1)

        best_subjects = sorted(subject_scores.values(), reverse=True)[:3] 
        total_ct_score = sum(best_subjects)  
        certificate_converted = avg_certificate * 10
        total_score = total_ct_score + certificate_converted  
        
        specialty = random.choice(specialties)
        city = random.choice(belarusian_cities)
        address = f"{city} , {fake.street_address()}" 
        phone = generate_belarusian_phone() 
        data.append({
            'ФИО': fio,
            'Год_поступления': year,
            'Форма_обучения': study_form,
            **subject_scores,
            'Средний_балл_аттестата': avg_certificate,
            'Общий_балл': total_score, 
            'Специальность': specialty,
            'Адрес': address,
            'Телефон': phone
        })
    
    return pd.DataFrame(data)

def visualize_data(df):
    plt.figure(figsize=(15, 12))

    plt.subplot(2, 2, 1)
    subjects = ['Математика', 'Физика', 'Химия', 'Биология', 'История', 'Русский язык']
    yearly_avg = df.groupby('Год_поступления')[subjects].mean()
    yearly_avg.plot(ax=plt.gca(), marker='o')
    plt.title('Динамика среднего балла ЦТ по предметам')
    plt.xlabel('Год поступления')
    plt.ylabel('Средний балл')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.subplot(2, 2, 2)
    certificate_avg = df.groupby('Год_поступления')['Средний_балл_аттестата'].mean()
    certificate_avg.plot(ax=plt.gca(), marker='o', color='red')
    plt.title('Динамика среднего балла аттестата')
    plt.xlabel('Год поступления')
    plt.ylabel('Средний балл аттестата')

    plt.subplot(2, 2, 3)
    specialty_counts = df['Специальность'].value_counts()
    specialty_counts.plot(kind='bar', ax=plt.gca(), color='green')
    plt.title('Количество поступивших по специальностям')
    plt.xlabel('Специальность')
    plt.ylabel('Количество студентов')
    plt.xticks(rotation=45)

    plt.subplot(2, 2, 4)
    study_form_counts = df['Форма_обучения'].value_counts()
    plt.pie(study_form_counts.values, labels=study_form_counts.index, autopct='%1.1f%%')
    plt.title('Распределение по формам обучения')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = generate_student_data(500)
    print("Первые 5 записей:")
    print(df.head())
    print("\nОсновная информация о данных:")
    print(df.info())
    print("\nОписательная статистика:")
    print(df.describe())
    
    visualize_data(df)
    
    df.to_csv('student_admission_data.csv', index=False, encoding='utf-8-sig')