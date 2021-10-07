# -*- coding: utf-8 -*-

# Предупреждения - Warnings
#
# Обычно используются для сообщений пользователю о ситуациях в ходе выполнения программы,
# которые не должны приводить к остановке программы.
#
# Часто можно видеть в библиотеках - они предупреждают что, пока работают,
# но в будущем могут сломаться...


# Бросить предупреждение - функция warnings.warn()
import warnings

greet_person = input('person_name: ')
if greet_person == 'Robert':
    # создаем обьект исключения и райзим его
    warnings.warn("We don't like you, Robert")
print(f'Hi there {greet_person}')
for i in range(10):
    print(i, end=' ')


# функция warn() может принимать категорию предупреждения
#
# Warning - This is the base class of all warning category classes.
#           It is a subclass of Exception.
# UserWarning - The default category for warn().
# DeprecationWarning - Base category for warnings about deprecated features
#           (ignored by default).
# SyntaxWarning - Base category for warnings about dubious syntactic features.
# RuntimeWarning - Base category for warnings about dubious runtime features.
# FutureWarning  - Base category for warnings about constructs that will change
#           semantically in the future.
# PendingDeprecationWarning - Base category for warnings about features that will be
#           deprecated in the future
#           (ignored by default).
# ImportWarning 	Base category for warnings triggered during
#           the process of importing a module
#           (ignored by default).
# UnicodeWarning 	Base category for warnings related to Unicode.
# BytesWarning 	Base category for warnings related to bytes and bytearray.
# ResourceWarning 	Base category for warnings related to resource usage.

import warnings

greet_person = input('person_name: ')
if greet_person == 'Robert':
    # создаем обьект исключения и райзим его
    warnings.warn("We don't like you, Robert", category=RuntimeWarning)
print(f'Hi there {greet_person}')
for i in range(10):
    print(i, end=' ')

# ловить варгинги нельзя! многие путаются
try:
    print(f'Hi there {greet_person}')
    print('Выполнение продолжается')
except RuntimeWarning:
    print('поймали RuntimeWarning!!!')
for i in range(10):
    print(i, end=' ')


# как временно отключить предупреждения?
#  - запустить скрипт с параметром -W "ignore"
#  - вызвать функцию simplefilter("ignore")

import warnings
warnings.simplefilter("ignore")
greet_person = input('person_name: ')
if greet_person == 'Robert':
    # создаем обьект исключения и райзим его
    warnings.warn("We don't like you, Robert")
print(f'Hi there {greet_person}')
for i in range(10):
    print(i, end=' ')


# более подробно см https://docs.python.org/3.6/library/warnings.html
