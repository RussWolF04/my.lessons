#   Задание
# '''
# 1. Создать список с фамилиями. Вывести все фамилии,
# которые начинаются на П и заканчиваются на а
# '''
# f = ["Петров", "Иванов", "Петришов", "Крючков", "Панин", "Кулакова", "Путина", "Пинина"]
# p = []
# for i in f:
#     if i[0] == 'П' and i[-1] == 'а':
#         p.append(i)
# print(p)
#
# '''
# 2. Дан список слов. Сгенерировать новый список с перевернутыми словами
# '''
# print(f[::-1])
#
# list_1 = ["Петров", "Иванов", "Петришов", "Крючков", "Панин", "Кулакова", "Путина", "Пинина"]
# list_2 = [23, 34, 43, 55, 23, 44, 56, 32]
# name = dict(zip(list_1, list_2))
# print(name)
#
# pupils = [
#     {
#         'firstname': 'Masha',
#         'Group': 42,
#         'physics': 7,
#         'informatics': 6,
#         'history': 8,
#     },
#     {
#         'firstname': 'sha',
#         'Group': 43,
#         'physics': 10,
#         'informatics': 6,
#         'history': 5,
#     },
#     {
#         'firstname': 'asha',
#         'Group': 44,
#         'physics': 4,
#         'informatics': 2,
#         'history': 5,
#
#     },
# ]
#
# average = 0
# count = 0
# for i in pupils:
#     for j in i:
#         if j != 'Group' and j != 'firstname':
#             count += 1
#             average += i[j]
#     average /= count
#     count = 0
#     i['average'] = average
#     average = 0
# for i in pupils:
#     if i['average'] > 4:
#         print(i['firstname'])
#
#
# import math
# a = [1, 2, 3, 4, 5, 6]
# print(sum(a))
#
# from functools import reduce  # Функция для свёрки последовательности
# from operator import mul  # Функция, перемножающая 2 числа
#
# spisok = [16, 15, 9, 14, 13]  # Исходный список
#
# result = reduce(mul, spisok)
# #                    /\ Список для свёртки
# #               /\ Используем умножение
# #        /\ Сворачиваем контейнер
# print(result)

print('     Задание №_8')
print('''
8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его
оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
баллов и посчитать средний балл по классу
''')
# with open("Class.txt", encoding='utf8') as file:
#     counter = 0
#     summa = 0
#     for line in file:
#         counter += 1
#         length_line = len(line)
#         for i in range(length_line):
#             if line[i].isdigit():
#                 num = int(line[i])
#                 summa += num
#                 if num < 3:
#                     print("Ученик, чья оценка по группе меньше 3-х:", line)
#                 break
#     average = summa / counter
#     print("Средний бал по группе:", average)

with open("Class.txt", encoding='utf8') as file:
    count = 0
    summa = 0
    name_student = [ ]

    for line in file:
        count += 1
        line_len = len(line)
        for i in range(line_len):
            if line[i].isdigit():
                num = int(line[i])
                summa += num
                average = summa / count
    print(f'Средний бал в классе = {round(average, 2)}\n')
    print(f'Список учеников у которых оценка = 3 баллам\n{name_student}')