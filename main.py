import json
import os
from itertools import combinations
import csv
from io import StringIO


def main(json_path):
    # Проверяем существование файла
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"File '{json_path}' not found.")

    # Читаем JSON из файла
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if len(data) == 0:
        raise ValueError("Input JSON data should contain at least one entity.")

    # Функция для генерации всех комбинаций признаков
    def generate_feature_combinations(item):
        features = list(item.keys())
        combinations_list = []
        for r in range(1, len(features) + 1):
            for comb in combinations(features, r):
                combinations_list.append(list(comb))
        return combinations_list

    # Функция для проверки уникальности комбинации признаков
    def unique_combination(combination, entities):
        key_set = set()
        for obj in entities:
            key = ''
            for feat in combination:
                if feat in obj:
                    key += str(obj[feat])
                else:
                    key += ''
            if key in key_set:
                return False
            key_set.add(key)
        return True

    # Находим минимальный по размеру набор признаков, который однозначно идентифицирует каждую сущность
    min_features = None
    min_size = float('inf')

    for item in data:
        combinations_list = generate_feature_combinations(item)
        for comb in combinations_list:
            if unique_combination(comb, data):
                if len(comb) < min_size:
                    min_size = len(comb)
                    min_features = comb

    if min_features:
        # Формируем CSV-строку
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["Features"])  # Шапка CSV
        for feat in min_features:
            writer.writerow([feat])  # Данные CSV

        csv_str = output.getvalue()
        output.close()
        return csv_str


# Пример использования
if __name__ == "__main__":
    json_file_path = './data.json'  # Пример пути к JSON-файлу
    csv_result = main(json_file_path)
    print(csv_result)





