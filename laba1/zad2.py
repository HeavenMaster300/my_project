number1 = int(input('Введите любое первое число: '))
number2 = int(input('Введите любое второе число: '))

if number1 > number2:
    print(f"Число {number1} является наибольшим из двух введённых, а число {number2} является наименьшим")
    count1 = number1 - number2
    print(f"Разница между числами равна {count1}")
else:
    print(f"Число {number2} является наибольшим из двух введённых, а число {number1} является наименьшим")
    count2 = number2 - number1
    print(f"Разница между числами равна {count2}")

if number1 == number2:
    print("Оба числа равны")
else:
    print("Числа не равны")

