# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой функции.

from typing import Callable
import json
import random

def deco(func: Callable):
    def wrapper(a, b, *arg, **args):
        fileName = str('{}'.format(func))[1:-1] # Достаем название функции для имени файла
        ind1 = str('{}'.format(func))[1:-1].index(' ')
        ind2 = str('{}'.format(func))[1:-1].index(' ', ind1 + 1)
        fileName = fileName[ind1 + 1:ind2]
        if not 1 <= a <= 100:
            a = random.randint(1, 100)
        if not 1 <= b <= 100:
            b = random.randint(1, 10)
        result = func(b, a)
        with open('{}'.format(fileName) + '.json', "a") as file:
            myDict = {}
            myDict['a'] = a
            myDict['b'] = b
            myDict.update(**args)
            json.dump(myDict, file)
        return result
    return wrapper

@deco
def fuTwo(count,x):
    while count > 0:
        number = int(input("Введите число: "))
        if number < x:
            print("Искомое больше ")
        elif number > x:
            print('Искомое меньше ')
        else:
            print("Угадали!")
            return count
        count -= 1
    return count

if __name__=="__main__":
    numb = int(input("Введите число от 1 до 100 для загадывания: "))
    count = int(input("Введите число от 1 до 10 - количество попыток для угадывания: "))
    fuTwo(numb, count)
    # fuTwo(5, 8, c=4)