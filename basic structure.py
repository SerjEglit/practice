# Для решения этой задачи, разберемся, что нам нужно сделать:
# Шаг 1. Понимание входных данных. У нас есть два типа данных:
# 1. Список grades, где каждый элемент — это список оценок одного ученика.
# Порядок в списке соответствует алфавитному порядку учеников.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# 2. Множество students, где содержатся имена учеников. Это множество неупорядоченно.
students = {'Сергей', 'Андрей', 'Натали', 'Татьяна', 'Александр'}
# Шаг 2. Алгоритм решения задачи
# 1. Перевести множество students в список: Поскольку множество неупорядоченно, нам нужно преобразовать его в список,
# чтобы мы могли сопоставить имена с оценками в нужном порядке.
# Для этого можно использовать функцию list().
# 2. Составить словарь с именами учеников и их средними баллами:
# - Мы знаем, что список grades уже упорядочен в алфавитном порядке.
# - Мы можем пройти по обоим объектам (по списку учеников и по списку оценок) и для каждого ученика вычислить средний балл.
# 3. Вычислить средний балл для каждого ученика:
# Для вычисления среднего балла используем стандартную формулу:\(\text{средний балл} = \frac{\sum \text{оценки}}{\text{количество оценок}}\).
# 4. Составить словарь: Ключом будет имя ученика, а значением — его средний балл.
# Шаг 3. Реализация. Теперь можно написать сам код.
# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Сергей', 'Андрей', 'Натали', 'Татьяна', 'Александр'}
# 1. Переводим множество students в отсортированный список
sorted_students = sorted(students)  # 2. Создаем пустой словарь для хранения средних баллов
average_grades = {}  # 3. Создаем словарь для сопоставления студентов и их оценок
student_grades = dict(zip(sorted_students, grades))  # 4. Пройдем по отсортированным ученикам и соответствующим оценкам

for student, grade_list in student_grades.items():
    average_grade = sum(grade_list) / len(grade_list)  # 5. Вычисляем средний балл
    average_grades[student] = average_grade  # 6. Добавляем запись в словарь

# 7. Выводим результат
print(average_grades)
print("Средние баллы студентов:")
for student, avg_grade in average_grades.items():
    print(f'{student}: {avg_grade:.2f}')
    # Также выводим список оценок каждого студента
    print("\nОценки студентов:")
for student, grade_list in student_grades.items():
    print(f'{student}: {grade_list}')

# Пояснение к результату
# - Александр: Средний балл \( (5 + 3 + 3 + 5 + 4) / 5 = 4.0 \)
# - Андрей: Средний балл \( (2 + 2 + 2 + 3) / 4 = 2.25 \)
# - Натали: Средний балл \( (5 + 3 + 3 + 5 + 4) / 5 = 4.0 \)
# - Сергей: Средний балл \( (4 + 4 + 3) / 3 = 3.6666 \)
# - Татьяна: Средний балл \( (5 + 5 + 5 + 4 + 5) / 5 = 4.8 \)

# Пояснения
# 1. Множество студентов: Множество (set) не сохраняет порядок, поэтому мы сначала преобразуем его в отсортированный список sorted(students). Это важно для корректного сопоставления студентов и оценок.
# 2. Создание словаря student_grades: Мы сопоставляем отсортированных студентов с их оценками с помощью zip().
# 3. Вычисление среднего балла: Для каждого студента из словаря мы вычисляем средний балл, используя sum(grade_list) / len(grade_list), и добавляем его в новый словарь average_grades.
# 4. Вывод: Мы выводим как средний балл, так и список оценок для каждого студента.
