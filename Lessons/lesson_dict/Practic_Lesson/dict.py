# Practic Lesson
# №_1
"""
Дана строка в виде случайной последовательности чисел от 0 до 9.
Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
а в качестве значений – количество этих чисел в имеющейся последовательности.
"""
import random
# str_1 = ''
# for i in range(10):
#     str_1 += str(random.randint(0, 9))
# print(str_1)
# my_dict = {}
# for i in str_1:
#     my_dict[int(i)] = str(str_1.count(i))
# print(my_dict)

# №_2
"""
Напишите программу, которая принимает аргумент в виде списка и возвращает словарь,
в котором каждый элемент списка является и ключом и значением.
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
"""
# my_list = [str(random.randint(1, 100)) for i in range(10)]
# my_dict = {}
# for i in my_list:
#     my_dict[str(i)] = i
#
# print(my_dict)

# №_3
"""
Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь.
"""

from collections import OrderedDict
dct = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})

# Меняем местами первый и последний элементы
first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)
print(dct)
# Удаляем второй элемент
second = list(dct.items())[1]
del dct[second[0]]
print(dct)
# Вставляем новый элемент
dct['new_key'] = 'new_value'
print(dct)