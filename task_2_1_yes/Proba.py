# s = input()
# count = 0
# flag = 0
# for i in range(len(s)):
#     if s[i] != ' ' and flag == 0:
#         count += 1
#         flag = 1
#     else:
#         if s[i] == ' ':
#             flag = 0
# print(count)

# что бы выполнить задание №_3 использую функцию len
# Функция len() в Python, считает количество элементов

#Метод python count() подсчитывает количество вхождений элемента в списке
# и возвращает найденое значение. Метод count() принимает один аргумент x,
# значение которое нужно найти. Данный метод возвращает количество вхождений элемента в список

# Метод split() разбивает строку по пробелам (по умолчанию) или символам,
# которые передаются как аргументы. Возвращает список.

# str = input("Введите текст: ")
# for i in range(len(str)):

# str = input("Ввдите тект: ")
# str = str.split() # spli() разбивает строку на пробелы
# l = len(str) # len() подсчитывает количество элементов
# if l > 5:
#     print(l)
# elif l < 5:
#     print("Need more!")
# elif l == 5:
#     print("It is five")

# a = int(input("Введите число: "))
# if type(a) == int: # делаем проверку на то что int является числом
#     print(a ** 3)

# from typing import List

rub = int(input("Введите количество рублей: "))
kop = int(input("Введите количество копеек: "))
kop_1 = [1, 21, 31, 41, 51, 61, 71, 81, 91]
kop_2 =[2, 3, 4, 22, 23, 24]
if rub == 1:
    if kop in  kop_1:
        print(rub, "рубль", kop, 'копейка')
    elif kop > 1 and kop < 5:
        print(rub, "рубль", kop, 'копейки')
    elif kop == 0 or kop > 4:
        print(rub, 'рубль', kop, 'копеек')
elif rub > 1 and rub < 5:
    if kop == 1:
        print(rub, "рубля", kop, 'копейка')
    elif kop > 1 and kop < 5:
        print(rub, "рубля", kop, 'копейки')
    elif kop == 0 or kop > 4:
        print(rub, 'рубля', kop, 'копеек')
elif rub == 0 or rub > 4:
    if kop == 1:
        print(rub, "рублей", kop, 'копейка')
    elif kop > 1 and kop < 5:
        print(rub, "рублей", kop, 'копейки')
    elif kop == 0 or kop > 4:
        print(rub, 'рублей', kop, 'копеек')