number = int(input('Введите любое число: '))

factorial = 1
for i in range(1,4):
    factorial *= i
print(factorial)

factorial = 1
for i in range(1,6):
    factorial *= i
print(factorial)

factorial = 1
for i in range(1,number+1):
    factorial *= i
print(factorial)

factorial = 1
while True:
    n = int(input('Введите 0 для завершения: '))
    factorial = 1
    if n != 0:
        for i in range(1,n+1):
            factorial *= i
        print(factorial)
    else:
        break
