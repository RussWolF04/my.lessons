'''4. Посчитать, сколько раз встречается определенная цифра в числах. Количество
введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
рандомно.'''

import random

kol = int(input('Количество: '))
isk = int(input('Искомая: '))
sp_chisl = ''
count = 0
while kol != 0:
    cif = random.randint(1, 100)
    if str(isk) in str(cif):
        count += 1
    sp_chisl += str(cif) + ''
    kol -= 1
print('Радномных чисел', sp_chisl)
print(f'Количество встречных цифр {isk} в числах: {count}')