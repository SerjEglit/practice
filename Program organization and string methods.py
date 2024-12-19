# 1. Ввод строки от пользователя
my_string = input("Введите произвольный текст: ")
# 2. Вывод количества символов в строке
print(f"Количество символов в введённом тексте: {len(my_string)}")
# 3. Работа с методами строк:
# 3.1. Преобразование строки в верхний регистр
upper_case = my_string.upper()
print(f"Строка в верхнем регистре: {upper_case}")
# 3.2. Преобразование строки в нижний регистр
lower_case = my_string.lower()
print(f"Строка в нижнем регистре: {lower_case}")
# 3.3. Удаление всех пробелов из строки
no_spaces = my_string.replace(" ", "#")
print(no_spaces)
# 3.4. Вывод первого символа строки
first_char = my_string[0] if my_string else "Строка пуста"
print(f"Первый символ строки: {first_char}")
# 3.5. Вывод последнего символа строки
last_char = my_string[-1] if my_string else "Строка пуста"
print(f"Последний символ строки: {last_char}")
