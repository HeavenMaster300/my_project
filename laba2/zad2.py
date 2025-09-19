import random
numbers = [random.randint(-50, 50) for _ in range(10)]
print(f"Исходный список: {numbers}")

#
even_numbers= []
for num in numbers:
    if num % 2 ==0:
        even_numbers.append(num)
print(f"\nЧётные элементы: {even_numbers}")

#
max_num = max(numbers)
min_num = min(numbers)
print(f'\nМинальное число: {min_num} и максимальное число: {max_num} в списке {numbers}')

#
print('\nВведите пять чисел для составления списка: ')
spisok = []

for i in range(1, 6):
    spisok.append(int(input()))

spisok.sort()
print(f'Отсортированный список с веденными числами: {spisok}')

#
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"\nСписок без дубликатов: {unique_numbers}")

#
if numbers:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    print(f"\nСписок после обмена первого и последнего элементов: {numbers}")