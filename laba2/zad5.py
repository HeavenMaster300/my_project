import random

# 1. Сгенерировать список из 20 случайных чисел и вывести только уникальные значения
numbers = [random.randint(-100, 100) for _ in range(20)]
unique_numbers = list(set(numbers))
print(f"Исходный список: {numbers}")
print(f"Уникальные значения: {unique_numbers}")

# 2. Создать словарь с количеством повторений элементов списка
number_counts = {}
for num in numbers:
    number_counts[num] = number_counts.get(num, 0) + 1
print(f"Словарь повторений: {number_counts}")

# 3. Создать множество из слов, длина которых больше 5 символов
words = ["кот", "собака", "питон", "программирование", "книга", "компьютер", "код", "алгоритм"]
long_words = {word for word in words if len(word) > 5}
print(f"Слова: {words}")
print(f"Множество слов длиннее 5 символов: {long_words}")

# 4. Ввести предложение и подсчитать вхождения каждого слова
sentence = input("Введите предложение: ")
words_in_sentence = sentence.lower().split()
word_counts = {}
for word in words_in_sentence:
    word_counts[word] = word_counts.get(word, 0) + 1
print(f"Словарь вхождений слов: {word_counts}")

# 5. Создать список чисел, преобразовать в множество и обратно в список
number_list = [random.randint(1, 10) for _ in range(15)]
number_set = set(number_list)
unique_list = list(number_set)
print(f"Исходный список: {number_list}")
print(f"Список без дубликатов: {unique_list}")

# 6. Найти самый дорогой товар в словаре
products = {"хлеб": 50, "молоко": 80, "яблоки": 120, "сыр": 300, "мясо": 450}
most_expensive = max(products.items(), key=lambda x: x[1])
print(f"Словарь товаров: {products}")
print(f"Самый дорогой товар: {most_expensive[0]} (цена: {most_expensive[1]})")

# 7. Определить повторяющиеся имена и самое частое имя
names = ["Анна", "Иван", "Мария", "Иван", "Анна", "Сергей", "Мария", "Анна", "Петр"]
name_counts = {}
for name in names:
    name_counts[name] = name_counts.get(name, 0) + 1
repeated_names = {name: count for name, count in name_counts.items() if count > 1}
most_common_name = max(name_counts.items(), key=lambda x: x[1])[0]
print(f"Список имён: {names}")
print(f"Повторяющиеся имена: {repeated_names}")
print(f"Самое частое имя: {most_common_name}")

# 8. Составить словарь: символ → индекс первого вхождения
user_string = input("Введите строку: ")
char_index = {}
for index, char in enumerate(user_string):
    if char not in char_index:
        char_index[char] = index
print(f"Словарь первых вхождений символов: {char_index}")