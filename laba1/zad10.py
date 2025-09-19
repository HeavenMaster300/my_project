# Циклы с условием

# Задание 10.1: Сумма чисел, пока не введут 0
sum_numbers = 0
while True:
    try:
        num = int(input("Введите число (0 для выхода): "))
        if num == 0:
            break
        sum_numbers += num
    except ValueError:
        print("Ошибка: введите целое число.")
print("Сумма =", sum_numbers)

# Задание 10.2: Количество чисел, пока не введут отрицательное
count = 0
while True:
    try:
        num = int(input("Введите число (отрицательное для выхода): "))
        if num < 0:
            break
        count += 1
    except ValueError:
        print("Ошибка: введите целое число.")
print("Количество чисел =", count)

# Задание 10.3: Сумма нечётных чисел, пока не введут чётное
sum_odd = 0
while True:
    try:
        num = int(input("Введите число (чётное для выхода): "))
        if num % 2 == 0:
            break
        sum_odd += num
    except ValueError:
        print("Ошибка: введите целое число.")
print("Сумма нечётных =", sum_odd)

# Задание 10.4: Среднее арифметическое, пока не введут число больше 100
total = 0
count = 0
while True:
    try:
        num = int(input("Введите число (больше 100 для выхода): "))
        if num > 100:
            break
        total += num
        count += 1
    except ValueError:
        print("Ошибка: введите целое число.")
if count > 0:
    print("Среднее =", total / count)
else:
    print("Числа не введены.")