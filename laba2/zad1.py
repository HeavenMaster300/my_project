for i in range(1, 11):
    print(f'\nТаблица умножения для {i}')
    for j in range(1, 11):
        result = j * i
        print(f'{i} * {j} = {result}')

summa = 0
for i in range(1, 101):
    if i % 2 != 0:
        summa += i
print(f'\nСумма всех нечетных чисел равна {summa}')

number = int(input("\nВведите число у которого хотите узнать все делители: "))
print(f'\nДелите числа {number}')
for i in range(1, number+1):
    if number % i == 0:
        print(f'{i}')

number2 = int(input("\nВведите число факториал которого хотите узнать: "))
print(f'\nФакториал числа {number2}:')
fact = 1
for i in range(1, number2+1):
    fact *= i
print(fact)

number3 = int(input("\nВведите длину для формирования последовательности Фибоначи: "))
fibonachi = [0, 1]
for i in range(2, number3):
    fibonachi.append(fibonachi[i-1] + fibonachi[i-2])
print(f'\nПоследовательность Фибоначи длиной {number3}')
print(fibonachi[:number3])