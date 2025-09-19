result = 0

for i in range(1,11):
    result = i + result

print(f'{result} результат сложения числел от 1 до 10')

number = int(input('Введите число до которого будет идти сложение: '))
result = 0

for i in range(1,number+1):
    result = i + result

print(f'{result} результат сложения числел от 1 до {number}')
result = 0

for i in range(1,number+1):
    if i % 2 == 0:
        result = i + result

print(f'{result} результат сложения четных числел от 1 до {number}')
result = 0

for i in range(1,number+1):
    if i % 2 != 0:
        result = i + result

print(f'{result} результат сложения нечетных числел от 1 до {number}')