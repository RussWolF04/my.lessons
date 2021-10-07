# -*- coding: utf-8 -*-

# for <переменная цикла> in <список>:
#     <блок кода>


# Цикл for ("для каждого элемента")
zoo_pets = ('lion', 'elephant', 'monkey', 'skunk', 'horse')
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
print('Выход из цикла')

zoo_pets = ('lion', 'elephant', 'monkey', 'skunk', 'horse')
letters_count = 0
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    letters_count += len(animal)
    pass
print('Всего букв', letters_count)

# принудительный останов цикла - break
zoo_pets = ('lion', 'elephant', 'monkey', 'skunk', 'horse')
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
print('Выход из цикла')

# опция else для цикла
zoo_pets = ('lion', 'elephant', 'monkey', 'skunk', 'horse')
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
else:
    print('Тут слона нет...')
print('Выход из цикла')

# пропуск остатка цикла - continue
zoo_pets = ['lion', 'skunk', 'elephant', 'monkey', 'horse']
for animal in zoo_pets:
    if animal == 'skunk':
        continue
    print('У нас в руках', animal)
print('Выход из цикла')

# полный пример

zoo_pets = (
    'lion', 'monkey', 'skunk',
    'elephant', 'horse',
)
for animal in zoo_pets:
    if animal == 'skunk':
        print('Сейчас переменная animal указывает на', animal)
        print('Фууу...')
        continue
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
else:
    print('Тут слона нет...')
print('Выход из цикла')


# Изменять содержимое последовательности, по которой проходит цикл, небезопасно
zoo_pets = [
    'lion', 'skunk',
    'elephant', 'horse',
]
for animal in zoo_pets:
    print(animal)
    del zoo_pets[0]
print(zoo_pets)



# полезные функции

# for(i=0; i < 10; i++) {
#       animal = zoo_pets[i];
#       printf(i, animal);
# }

for i, animal in enumerate(zoo_pets):
    print(i, animal)

# генерация целочисленных последовательностей
for i in range(100, 600, 50):
    print(i)

# НЕ ДЕЛАЙТЕ ТАК!!!!
zoo_pets = ['lion', 'skunk', 'elephant', 'horse', ]
for i in range(len(zoo_pets)):
    animal = zoo_pets[i]
    print(i, animal)


# вложенные циклы
zoo_pets = [
    'lion', 'skunk',
    'elephant', 'horse',
]
for animal in zoo_pets:
    for char in animal:
        print(char)
    print(animal)


