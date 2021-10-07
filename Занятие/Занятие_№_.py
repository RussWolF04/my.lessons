# Алфавит
# for i in range(65, 120):
#     print(chr(i), end= ' ')
# import random
#
# a = [random.randint(1, 40) for i in range(20)]
# b = [random.randint(1, 40) for i in range(20)]
# if sum(a) > sum(b) and sum(a) != sum(b):
#     print(f'Сумма Картежа "а" - {sum(a)} > Суммы Картежа "b" - {sum(b)}')
# elif sum(a) < sum(b) and sum(a) != sum(b):
#     print(f'Сумма Картежа "а" - {sum(a)} < Суммы Картежа "b" - {sum(b)}')
# else:
#     print(f'Каржи равны')
#
# print(f'Tuple "a" = {a}\nTuple "b" = {b}')
# print(f'Сумма Картежа "а" = {sum(a)}')
# print(f'Сумма картежа "b" = {sum(b)}')
# print(f'Minimum "a" = {a.index(min(a))}  Maximum "a" = {a.index(max(a))}')
# print(f'Minimum "b" = {b.index(min(b))}  Maximum "b" = {b.index(max(b))}')
# print(f'Общее произведение Картежа "а" и "b" = {sum(a) * sum(b)}')

# lst = [1,2,3]
# lst_rev = [3,2,1]
# g = [(x,y) for x in lst for y in lst_rev]
# print(g)

# Генераторы множеств
# '''
#  1. Генератор множества – это выражение и цикл с необязательным
# условием, заключенные в фигурные скобки.
#  2. Подобно генераторам списков, генераторы множеств поддерживают две
# формы записи:
# {expression for item in iterable}
# {expression for item in iterable if condition}'''
# # Пример Генератора Множеств
# m = {x for x in range(20) if x % 2 == 0}
# print(m)

# Вложенные списки
# ДО:
# xlList = [[1,2,3], [4,5,6], [7,8,9]]
# myList = []
# for sList in xlList:
#     for item in sList:
#         myList.append(item)
# print(myList)
# ПОСЛЕ:
# xlList = [[1,2,3], [4,5,6], [7,8,9]]
# myList = [item for sList in xlList for item in sList]
# print(myList)


# Вложенные УСЛОВИЯ
# ДО:
# aList = []
# for i in range(10):
#     if i%3 == 0:
#         aList.append(i)
# print(aList)
# # ПОСЛЕ:
# aList = [i for i in range(10) if i%3 == 0]
# print(aList)

