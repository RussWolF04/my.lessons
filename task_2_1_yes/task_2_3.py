# № 3.
# Ввести строку с клавиатуры
# Если длина строки больше 5 - вывести значение на экран
# Если длина строки меньше 5 - вывести строку
# “Need more!” Если длина строки равна 5 - вывести
# строку “It is five”
# Т.е., нем нужно узнать сколько слов в тексте

# Функция len() в Python, считает количество элементов

# Метод split() разбивает строку по пробелам (по умолчанию) или символам,
# которые передаются как аргументы. Возвращает список.

str = input("Ввдите тект: ")
str = str.split() # spli() разбивает строку на пробелы
l = len(str) # len() подсчитывает количество элементов
if l > 5:
    print(l)
elif l < 5:
    print("Need more!")
elif l == 5:
    print("It is five")