# Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.

import random
from typing import Callable

def deco(func: Callable):
    def wrapper(a, b, *arg, **args):
        print(a,b)    
        if not 1 <= a <= 100:
            a = random.randint(1, 100)
        if not 1 <= b <= 10:
            b = random.randint(1, 10)
        result = func(b, a)
        return result
    return wrapper

@deco
def fuTwo(count,x):
    print(count, x)
    while count > 0:
        number = int(input("Введите число: "))
        if number < x:
            print("Не угадали, искомое число больше")
        elif number > x:
            print("Не угадали, искомое число меньше")
        else:
            print("Ура, Вы угадали!")
            return count
        count -= 1
    return count

if __name__ == "__main__":
    numb = int(input("Введите число от 1 до 100 для загадывания: "))
    count = int(input("Введите число от 1 до 10 - количество попыток для угадывания: "))
    fuTwo(numb, count)