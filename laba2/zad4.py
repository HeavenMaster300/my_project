import random

# 1. Создать два множества и вывести их пересечение и объединение
set1 = {random.randint(1, 20) for _ in range(10)}
set2 = {random.randint(1, 20) for _ in range(10)}
print(f"Множество 1: {set1}")
print(f"Множество 2: {set2}")
print(f"Пересечение: {set1.intersection(set2)}")
print(f"Объединение: {set1.union(set2)}")

# 2. Найти все уникальные слова в тексте, введённом пользователем
text = input("\nВведите текст: ")
words = text.lower().split()  # Разбиваем текст на слова и приводим к нижнему регистру
unique_words = set(words)
print(f"Уникальные слова: {unique_words}")

# 3. Найти общие элементы двух списков с помощью множеств
list1 = [random.randint(-10, 10) for _ in range(8)]
list2 = [random.randint(-10, 10) for _ in range(8)]
set_list1 = set(list1)
set_list2 = set(list2)
common_elements = set_list1.intersection(set_list2)
print(f"\nСписок 1: {list1}")
print(f"Список 2: {list2}")
print(f"Общие элементы: {common_elements}")

# 4. Проверить, является ли одно множество подмножеством другого
is_subset = set1.issubset(set2)
print(f"\nЯвляется ли множество 1 подмножеством множества 2? {is_subset}")

# 5. Удалить из множества все элементы, которые меньше заданного числа
threshold = int(input("\nВведите число для удаления элементов меньше него: "))
set_to_filter = {random.randint(-50, 50) for _ in range(10)}
print(f"Исходное множество: {set_to_filter}")
set_to_filter = {x for x in set_to_filter if x >= threshold}
print(f"Множество после удаления элементов меньше {threshold}: {set_to_filter}")