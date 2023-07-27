# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

def add_one(numb, count):
    def add_two():
        nonlocal count
        while count > 0:
            n = int(input("Какое число? "))
            if n != numb:
                print("Неверно")
                count -= 1
                continue
            else:
                print("Ура, Вы угадали!")
                break

    return add_two
  
    
if __name__ == "__main__":
        
    numb = int(input("Введите число от 1 до 100 для загадывания: "))
    count = int(input("Введите число от 1 до 10 - количество попыток для угадывания: "))
    h = add_one(numb, count)
    h()
    # h1 = add_one(numb, count)()