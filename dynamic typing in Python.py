# Модуль: module_1_3.py
# Цель: Полная демонстрация динамической типизации в Python

# Переменная типа строка (string)
name = "Иван"  # Присваиваем строковое значение
print(f"Name: {name}, Type: {type(name)}")  # Выводим значение и тип переменной

# Переменная типа целое число (integer)
age = 25  # Присваиваем целочисленное значение
print(f"Age: {age}, Type: {type(age)}")

# Обновление переменной 'age' на основе текущего значения
age += 1  # Увеличиваем значение 'age' на 1
print(f"Updated Age: {age}, Type: {type(age)}")

# Переменная типа вещественное число (float)
height = 175.5  # Присваиваем вещественное значение
print(f"Height: {height} cm, Type: {type(height)}")

# Переменная типа логическое значение (boolean)
is_student = True  # Присваиваем логическое значение
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# Переменная типа список (list)
hobbies = ["reading", "cycling", "programming"]  # Список увлечений
print(f"Hobbies: {hobbies}, Type: {type(hobbies)}")

# Обновление списка: добавление нового увлечения
hobbies.append("gaming")  # Добавляем новый элемент в список
print(f"Updated Hobbies: {hobbies}")

# Переменная типа словарь (dictionary)
profile = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}  # Создаем словарь с данными
print(f"Profile: {profile}, Type: {type(profile)}")

# Изменение значения в словаре
profile["age"] += 5  # Увеличиваем возраст на 5 в словаре
print(f"Updated Profile: {profile}")

# Переменная, меняющая тип на лету
variable = 10  # Изначально переменная имеет тип int
print(f"Variable (int): {variable}, Type: {type(variable)}")

variable = "Python"  # Теперь переменная становится строкой
print(f"Variable (string): {variable}, Type: {type(variable)}")

variable = [1, 2, 3]  # Теперь переменная становится списком
print(f"Variable (list): {variable}, Type: {type(variable)}")

# Переменная с функцией как значением
def greet():
    return "Hello, World!"

function_variable = greet  # Присваиваем функцию переменной
print(f"Function Variable: {function_variable()}, Type: {type(function_variable)}")

# Приведение типов
value = "123"  # Изначально строка
print(f"Value (string): {value}, Type: {type(value)}")

value = int(value)  # Преобразуем строку в число
print(f"Value (int): {value}, Type: {type(value)}")

value = float(value)  # Преобразуем число в float
print(f"Value (float): {value}, Type: {type(value)}")

# Сложные структуры данных (вложенные списки и словари)
data = {
    "name": "Alice",
    "scores": [95, 88, 92],  # Вложенный список
    "details": {
        "age": 20,
        "student": True
    }  # Вложенный словарь
}
print(f"Data: {data}")
print(f"Name: {data['name']}, Age: {data['details']['age']}")

# Работа с переменной типа None
optional_field = None  # Переменная с пустым значением
print(f"Optional Field: {optional_field}, Type: {type(optional_field)}")

# Смена значения через условия
user_input = "yes"  # Например, ввод пользователя
is_confirmed = True if user_input.lower() == "yes" else False
print(f"Confirmation: {is_confirmed}, Type: {type(is_confirmed)}")
