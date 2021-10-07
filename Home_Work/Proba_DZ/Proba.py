# import os
# import books as np
# path = "C:/Users/Evgeniy/PycharmProject/IT_OverOne/Home_Work/Proba_DZ/books"
#
# for filename in os.listdir(path):
#     foldername = path + "//" + filename
#     print(foldername)
# word = input('Entry word: ')
# for word in os.listdir(path):
#     foldername = path + '//' + word
#     path = word
#     print(word)
import pathlib

import os
# определение текущей рабочей директории
path = 'C:/Users/Evgeniy/PycharmProject/IT_OverOne/Home_Work/Proba_DZ/books'
#
# # чтение записей
# with os.scandir(path) as books:
#     for entry in books:
#         # печать всех записей, являющихся файлами
#         if entry.is_file():
#             print(entry.name)




# directory = r'C:/Users/Evgeniy/PycharmProject/IT_OverOne/Home_Work/Proba_DZ/books'
file = '*.txt'
word = input(r'Entry word: ')

for path in pathlib.Path(path).rglob(file):
    with open(path) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if word in lines[i]:
                print(f'Путь: {path}\n'
                       'Строки:')
                if i == 0:
                    print(lines[0])
                elif i == 1:
                    print(*lines[:2], sep='')
                else:
                    print(*lines[i-2:i+1], sep='')
