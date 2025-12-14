import requests
from bs4 import BeautifulSoup
import csv
import time
import argparse
import os
from urllib.parse import quote
import re

class WikipediaScraper:
    def __init__(self, cache_dir="cache"):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def get_page(self, country_name):
        cache_file = os.path.join(self.cache_dir, f"{country_name.replace(' ', '_')}.html")

        if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='utf-8') as f:
                return f.read()

        url = f"https://en.wikipedia.org/wiki/{quote(country_name.replace(' ', '_'))}"
        try:
            response = self.session.get(url)
            response.raise_for_status()

            with open(cache_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            return response.text
        except requests.RequestException as e:
            print(f"Ошибка при загрузке страницы для {country_name}: {e}")
            return None

    def parse_country_info(self, html, country_name):
        """Парсит информацию о стране из HTML"""
        if not html:
            return None, None, None
        
        soup = BeautifulSoup(html, 'html.parser')

        infobox = soup.find('table', {'class': re.compile(r'infobox.*country|vcard')})
        if not infobox:
            infobox = soup.find('table', {'class': 'infobox'})
        
        if not infobox:
            print(f"Не найдена информационная таблица для {country_name}")
            return None, None, None
        
        capital = self.extract_capital(infobox)
        area = self.extract_area(infobox)
        population = self.extract_population(infobox)
        
        return capital, area, population

    def extract_capital(self, infobox):
        """Извлекает столицу"""
        try:
            capital_row = infobox.find('th', string=re.compile(r'Capital', re.I))
            if capital_row:
                capital_cell = capital_row.find_next('td')
                if capital_cell:
                    capital_link = capital_cell.find('a')
                    if capital_link:
                        return capital_link.get_text().strip()
            return None
        except Exception as e:
            print(f"Ошибка при извлечении столицы: {e}")
            return None

    def extract_area(self, infobox):
        """Извлекает площадь"""
        try:
            area_row = infobox.find('th', string=re.compile(r'Area', re.I))
            if not area_row:
                area_row = infobox.find('th', string=re.compile(r'Total', re.I))
            
            if area_row:
                area_cell = area_row.find_next('td')
                if area_cell:
                    area_text = area_cell.get_text()
                    match = re.search(r'(\d{1,3}(?:,\d{3})*)\s*km²', area_text)
                    if match:
                        area_str = match.group(1).replace(',', '')
                        return int(area_str)
            return None
        except Exception as e:
            print(f"Ошибка при извлечении площади: {e}")
            return None

    def extract_population(self, infobox):
        """Извлекает население"""
        try:
            pop_row = infobox.find('th', string=re.compile(r'Population', re.I))
            if pop_row:
                pop_cell = pop_row.find_next('td')
                if pop_cell:
                    pop_text = pop_cell.get_text()
                    numbers = re.findall(r'\d{1,3}(?:,\d{3})*', pop_text)
                    if numbers:
                        pop_str = numbers[-1].replace(',', '')
                        return int(pop_str)
            return None
        except Exception as e:
            print(f"Ошибка при извлечении населения: {e}")
            return None

def read_countries(input_file):
    """Читает список стран из файла"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            countries = [line.strip() for line in f if line.strip()]
        return countries
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла {input_file}: {e}")
        return []

def write_to_csv(data, output_file):
    """Записывает данные в CSV файл"""
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['country', 'city', 'area', 'population'])
            for row in data:
                writer.writerow(row)
        print(f"Данные сохранены в {output_file}")
    except Exception as e:
        print(f"Ошибка при записи в CSV: {e}")

def clean_number(number_str):
    """Очищает число от запятых и других символов"""
    if not number_str:
        return None
    return re.sub(r'[^\d]', '', str(number_str))

def main():
    parser = argparse.ArgumentParser(description='Scrape country data from Wikipedia')
    parser.add_argument('-i', '--input', default='countries.txt', 
                       help='Input file with country names (default: countries.txt)')
    parser.add_argument('-o', '--output', default='countries_data.csv', 
                       help='Output CSV file (default: countries_data.csv)')
    
    args = parser.parse_args()

    countries = read_countries(args.input)
    if not countries:
        print("Не удалось прочитать список стран")
        return
    
    print(f"Найдено {len(countries)} стран для обработки")

    scraper = WikipediaScraper()
    results = []

    for i, country in enumerate(countries, 1):
        print(f"Обрабатывается {country} ({i}/{len(countries)})...")

        html = scraper.get_page(country)
        
        if html:
            capital, area, population = scraper.parse_country_info(html, country)
            
            if capital or area or population:
                results.append([country, capital or 'N/A', area or 'N/A', population or 'N/A'])
                print(f"  ✓ Столица: {capital}, Площадь: {area}, Население: {population}")
            else:
                results.append([country, 'N/A', 'N/A', 'N/A'])
                print(f"  ✗ Не удалось извлечь данные")
        else:
            results.append([country, 'N/A', 'N/A', 'N/A'])
            print(f"  ✗ Не удалось загрузить страницу")

        if i < len(countries):
            time.sleep(1)

    write_to_csv(results, args.output)
    print(f"Обработка завершена. Успешно обработано: {len([r for r in results if r[1] != 'N/A'])} стран")

if __name__ == "__main__":
    main()