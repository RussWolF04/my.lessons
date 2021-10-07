parol = input('Введите пароль: ')
index_num = 0
index_char = 0
i = 0
for i in range(len(parol)):  # для поиска и подсчета количества букв и цифр
    if parol[i].isdigit() == 1:
        index_num += 1
    if parol[i].isalpha() == 1:
        index_char += 1
    i += 1

index_high = -1  # для поиска и подсчета номера заглавных и строчных букв
for index_high in range(len(parol) - 1):
    if parol[index_high].isupper() == 1:
        break
    index_high += 1
index_low = -1
for index_low in range(len(parol) - 1):
    if parol[index_low].islower() == 1:
        break
    index_low += 1

if index_num == 0:
    print('Пароль должен содержать хотя бы одну цифру ')
if index_num + index_char == len(parol):
    print('Пароль должен содержать хотя бы один символ ')
if index_char == 0:
    print('Пароль должен содержать хотя бы одну букву ')

if index_char != 0:                           # чекает последний символ для проверки на заглавную/строчную
    if index_high == len(parol) - 1:          # тк без этой прикалюхи оно не видело заглавную букву, если она
        if parol[index_high].isupper() != 1:  # была последней в строке               либо я daun
            print('В пароле должна быть хотя бы одна заглавная буква ')
    if index_low == len(parol) - 1:
        if parol[index_low].islower() != 1:
            print('В пароле должна быть хотя бы одна строчная буква ')

if ' ' in parol:
    print('В пароле не должно быть пробелов ')
if len(parol) < 8:
    print('В пароле должно быть минимум 8 символов ')

if len(parol) >= 8 and not ' ' in parol and index_num != 0 and index_char != 0 and index_num + index_char != len(
        parol) and parol[index_high].isupper() == 1 and parol[index_low].islower() == 1:

    if input('Повторите пароль: ') == parol:
        print("Новый пароль создан")
    else:
        print('Пароли не совпадают')

print('num ', index_num)
print('char ', index_char)
print('high ', index_high)
print('low', index_low)
print(len(parol))
print(index_num+index_char)