'''Напиши игру «Русская рулетка».
В начале вводится количество игроков и их имена.
Они сортируются по алфавиту.
На случайное место в револьвере (в списке)
ставится пуля. Потом пользователю дается
возможность «покрутить барабан» (выбрать
число от 1 до 6). Если на этом месте пуля – ты
выбыл. Если нет, то крутит следующий игрок.
**добавь статистику, где будет самый живучий и
самый невезучий игрок.'''
#       Алгоритм
# Ввести количество игроков: +
# Введите имена всех игроков которые участвуют: +
# Проверям на равенство числа играков и самих играков +
# Сортировка имен по алфавиту +
#
#
#

print('Введите количество игроков и их Имена')
kol_list = [] # Пустой список количества игроков
name_list = [] # Пустой список игроков
count = 0
# Количество игроков
kol = int(input("Сколько игроков играют?: "))
kol_list = [i for i in range(1, kol + 1)] # Генератор списка количества игроков
kol_list = len(kol_list)
print(f'Игроков учавствует - {kol_list}')
if kol == 0:
    print('Game Over\nНикто не пришел!')

# name_list = name_list.split()
name_int = len(name_list)

# Имена игроков
# if 0 > name_int != kol:
while count != kol:
    if count < kol:
        name_list.append(input(f'Представте участника №_{count + 1}: ').title())
        count += 1
    else:
        count == kol
        print(f'Все участники взборе.\nСписок игроков - {name_list}\nМожем начинать игру!!!')
# print(name_list)
name_list.sort()

print(name_list)