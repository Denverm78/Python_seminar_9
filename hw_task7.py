# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import random
from cmath import sqrt
import csv
import json
from pathlib import Path
from typing import Callable
from functools import wraps

COUNT_STR = 100
MIN_NUMBER = -100
MAX_NUMBER = 100

def from_csv_wrap(file_name):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_name, 'r', encoding='utf-8') as file_csv:
                reader = csv.reader(file_csv)
                for i, row in enumerate(reader):
                    if i == 0:
                        continue
                    args = (complex(j) for j in row)
                    result = func(*args, **kwargs)
                    yield result
        return wrapper
    return deco


def create_json(func):
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            file_json = json.load(f)
    else:
        file_json = []

    def wrapper(*args, **kwargs):
        for result in func(*args, **kwargs):
            if result:
                result_dict = {'args': args, **kwargs, 'result': str(result)}
                file_json.append(result_dict)
                with open(file, 'w', encoding='utf-8') as json_f:
                    json.dump(file_json, json_f, indent=2)
            else:
                break

    return wrapper


@create_json
@from_csv_wrap('result.csv')
def find_roots(a: complex, b: complex, c: complex):
    if a != 0:
        discr: complex = b * b - 4 * a * c
        x1: complex = (-b + sqrt(discr)) / (2 * a)
        x2: complex = (-b - sqrt(discr)) / (2 * a)
        return discr, x1, x2
    else:
        return 0, 0, 0


def create_csv(name: str = 'result', rows_count: int = COUNT_STR, min_num: int = MIN_NUMBER, max_num: int = MAX_NUMBER):
    rows = []
    for _ in range(rows_count):
        a, b, c = random.sample(range(min_num, max_num), 3)
        rows.append({'a': a, 'b': b, 'c': c})
    with open(name + '.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['a', 'b', 'c']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    create_csv()
    