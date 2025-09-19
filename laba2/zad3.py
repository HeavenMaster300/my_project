# 1. Создать словарь с именами студентов и их оценками, вывести средний балл
students = {
    "Алексей": 85,
    "Мария": 92,
    "Иван": 78,
    "Анна": 95,
    "Сергей": 88
}
average_score = sum(students.values()) / len(students)
print(f"Словарь студентов: {students}")
print(f"Средний балл: {average_score}")

# 2. Подсчитать количество каждой буквы в строке
user_string = input("Введите строку: ")
letter_count = {}
for char in user_string:
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1
print(f"Количество каждой буквы: {letter_count}")

# 3. Создать словарь с числами от 1 до 10 и их квадратами
squares = {i: i**2 for i in range(1, 11)}
print(f"Словарь квадратов: {squares}")

# 4. Составить словарь из двух списков
keys = ["имя", "возраст", "город"]
values = ["Алексей", 20, "Москва"]
combined_dict = dict(zip(keys, values))
print(f"Словарь из двух списков: {combined_dict}")