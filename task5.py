# Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.

import json
import random
from typing import Callable


def deco1(func: Callable):
    def wrapper(a, b, *arg, **args):
        result = func(a, b)
        return result
    return wrapper


def deco2(func: Callable):
    def wrapper(a, b, *arg, **args):
        print('Оборачиваемая функция: {}'.format(func))
        fileName = str('{}'.format(func))[1:-1]
        ind1 = str('{}'.format(func))[1:-1].index(' ')
        ind2 = str('{}'.format(func))[1:-1].index(' ', ind1 + 1)
        fileName = fileName[ind1 + 1:ind2]
        result = func(a, b)
        with open('{}'.format(fileName) + '.json', "a") as file:
            myDict = {}
            myDict['a'] = a
            myDict['b'] = b
            myDict.update(**args)
            json.dump(myDict, file)
        return result
    return wrapper


def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        return wrapper
    return deco


@count(10)
@deco1
@deco2
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)

if __name__=="__main__":
    print(rnd(1, 5))
