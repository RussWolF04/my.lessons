vd5 = 0
vd3 = 0
count = 0

# print(
#     '''Имеется 2 ведра, одно 3 литра другое 5 литров
# и неограниченное количество воды.
# Пользователь может
# 1. Набирать воду в любое ведро.
# 2. Выливать воду из любого ведра.
# 3. Переливать воду из одного ведра в другое.
# Пользователь побеждает если ему удаётся получить ровно 4 литра.'''
# )

while vd5 != 4:
    ask = int(input('''Давайте начнем:
               1. Наберем воды в 5-и литровое ведро?
               2. Наберем воды в 3-х литровое ведро?
               3. Наполнить два ведра водой?
                  Выбор: '''))
    while ask != 1 or ask != 2:
        # ask = int(input('''Давайте начнем:
        #                1. Наберем воды в 5-и литровое ведро?
        #                2. Наберем воды в 3-х литровое ведро?
        #                3. Наполнить два ведра водой?
        #                   Выбор: '''))
        if ask == 1: # Вариант №_2
            vd5 += 5 # Наполнили 5-и л.в. водой
            count += 1
            print(f'5-и литровое ведро = {vd5} литров')
            break
        elif ask == 2: # Вариант №_1
            vd3 += 3 # Наполнили 3-х л.в. водой
            count += 1
            print(f'3-х литровое ведро = {vd3} литра')
            break
        elif ask == 3:
            vd5 += 5
            vd3 += 3
            count += 1
            print(f'Что будем делать с полным 5-и литровым ведром = {vd5}л\nи с полным 3-х литровым ведром = {vd3}л ?')
            break
    while ask != 2 or ask != 3:
        ask = int(input('''Что делаем с ведрами воды:
            1. Перельем 5-и литровое в 3-х литровое ведро?
            2. Перельем 3-х литровое в 5-и литровое ведро?
            3. Выльем оба ведра?
               Выбираем: '''))
        if ask == 1: # Вариант №_2
            vd3 += 3 # Перелили из 5-и л.в.
            vd5 -= 3 # Осталось 2л в 5-и л.в.
            count += 1
            print(f'Теперь в 5-и литровом ведре осталось = {vd5}л\nа в 3-х литровом стало = {vd3}л')
            break
        elif ask == 2: # Вариант №_1
            vd5 += 3 # Перелили из 3-х л.в.
            vd3 -= 3 # Остаток 0
            count += 1
            print(f'Теперь в 5-и литровом ведре стало = {vd5}л\nа в 3-х литровом стало = {vd3}л')
            break
        elif ask == 3:
            vd5 -= 5
            vd3 -= 3
            count += 1
            print(f'Теперь в 5-и литровом ведре осталось = {vd5}л\nа в 3-х литровом осталось = {vd3}л')
            break
    while ask != 1 or ask != 2:
        ask = int(input('''Продолжай
            1. Выльем 3-х литровое ведро?
            2. Наполним 3-х литровое ведро водой?
            3. Пустые ведра наполняем на половину
               : '''))
        if ask == 1: # Вариант №_2
            vd3 -= 3 # Вылили воду из ведра
            # vd5 -= 2 # Остаток 0
            count += 1
            print(f'Остаток {vd5}л в 5-и л.в. в 3-х л.в. = {vd3}л')
            break
        elif ask == 2: # Вариант №_1
            vd3  += 3 # Наполнили 3л воды ведро 3-х литровое
            count += 1
            print(f'3-х литровое ведро = {vd3} литра 5-и л.в. остаток {vd5}')
            break
        elif ask == 3: # наполнили на половину оба ведра
            vd5 += 2.5
            vd3 += 1.5
            count += 1
            print(f'Наполнили ведра на половину 5лв = {vd5}л и 3лв = {vd3}л')
            break
    while ask != 1 or ask != 2:
        ask = int(input('''
            1. Доливаем в 5лв
            2. Переливаем остатки из 5лв в 3лв
            3. Переливаем половину 3лв в 5лв
               : '''))
        if ask == 1: # Вариант решения №_1
            vd5 += 2 # Долили до полного 5 литрового ведра водой
            vd3 -= 2 # В ведре остался 1 литр
            count += 1
            print(f'В ведре 3 осталось {vd3}л, а в ведре 5 стало {vd5}л')
            break
        elif ask == 2: # Вариант решения №_2
            vd3 += 2 # Перелили из 5лв в 3лв
            vd5 -= 2
            count += 1
            print(f'3-х литровое ведро = {vd3} литра 5-и л.в. остаток {vd5}')
            break
        elif ask == 3:
            vd5 += vd3
            vd3 -= 1.5
            count += 1
            print(f'воды в 5лв = {vd5}л, а в 3лв = {vd3}л')
            break
        ask = int(input('''
            1. Выльем воду из ?
            2. '''))

