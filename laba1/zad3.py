number = int(input(f"Введите число для таблицы умножения: "))
count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Таблица умножения для {number}")

for i in count:
    result = i * number
    print(result)