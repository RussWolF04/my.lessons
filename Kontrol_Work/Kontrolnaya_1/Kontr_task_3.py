'''3. Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно.
Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше
рандомной пары. Проверку выполнить 7 раз.
В случае равенства (количества, когда пара больше и всех остальных случаем)
вывести случайные числа, полученные в 4 итерации.
'''

import random
print("Введите 2 числа от 1 до 20")

from random import randint
num_r_1 = int(random.randint(1, 20))
num_r_2 = int(random.randint(1, 20))

hight_1 = 0
hight_2 = 0

low_1 = 0
low_2 = 0

count_1 = 0
count_2 = 0

total_1 = []
total_2 = []

num = int(input("Введите число №_1: "))
num_1 = int(input("Введите число №_2: "))

for i in range(7):
    if num > num_r_1:
        hight_1 += 1
        if num_1 > num_r_2:
            hight_2 += 1
    elif num == num_r_1:
        count_1 += 1
        if num_1 == num_r_2:
            count_2 += 1
    elif num < num_1:
        low_1 += 1
        if num_1 < num_r_2:
            low_2 += 1
if hight_1 == hight_2:
    total_1.append(num_r_1)
    total_2.append(num_r_2)
    print(f'{total_1} and {total_2}')
print(f'{num} > {num_r_1} = {hight_1} раз\n{num_1} > {num_r_2} = {hight_2} раз')