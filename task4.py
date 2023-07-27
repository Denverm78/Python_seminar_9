# Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции.

from typing import Callable
import random


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
def rnd(a: int, b: int):
    return random.randint(a, b) 

if __name__=="__main__":

    print(rnd(1, 5))   