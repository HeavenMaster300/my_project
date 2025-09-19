# Работа с цифрами числа

# Задание 8.1: Сумма цифр двузначного числа
while True:
    try:
        num = int(input("Введите двузначное число: "))
        if 10 <= num <= 99 or -99 <= num <= -10:
            digit1 = num // 10
            digit2 = num % 10
            print("Сумма цифр =", digit1 + digit2)
            break
        else:
            print("Ошибка: введите двузначное число.")
    except ValueError:
        print("Ошибка: введите целое число.")

# Задание 8.2: Произведение цифр двузначного числа
while True:
    try:
        num = int(input("Введите двузначное число: "))
        if 10 <= num <= 99 or -99 <= num <= -10:
            digit1 = num // 10
            digit2 = num % 10
            print("Произведение цифр =", digit1 * digit2)
            break
        else:
            print("Ошибка: введите двузначное число.")
    except ValueError:
        print("Ошибка: введите целое число.")

# Задание 8.3: Сумма цифр трёхзначного числа
while True:
    try:
        num = int(input("Введите трёхзначное число: "))
        if 100 <= num <= 999 or -999 <= num <= -100:
            digit1 = num // 100
            digit2 = (num // 10) % 10
            digit3 = num % 10
            print("Сумма цифр =", digit1 + digit2 + digit3)
            break
        else:
            print("Ошибка: введите трёхзначное число.")
    except ValueError:
        print("Ошибка: введите целое число.")

# Задание 8.4: Первая и последняя цифры трёхзначного числа
while True:
    try:
        num = int(input("Введите трёхзначное число: "))
        if 100 <= num <= 999 or -999 <= num <= -100:
            digit1 = num // 100
            digit3 = num % 10
            print("Первая цифра:", digit1, "Последняя цифра:", digit3)
            break
        else:
            print("Ошибка: введите трёхзначное число.")
    except ValueError:
        print("Ошибка: введите целое число.")