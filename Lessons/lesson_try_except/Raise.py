# -*- coding: utf-8 -*-

# Порождение исключений
# Зачастую нужно самим создавать исключение, если код не может справиться с данными


greet_person = input('person_name: ')
if greet_person == 'Robert':
    # создаем обьект исключения и райзим его
    raise BaseException("We don't like you, Robert")
print(f'Hi there {greet_person}')


##################
# Варианты порождения исключений

greet_person = input('person_name: ')
if greet_person == 'Robert':
    # создаем обьект исключения и райзим его
    raise BaseException
print(f'Hi there {greet_person}')

# но так лучше не делать - старый стиль

# в сети иногда попадаются старинные варианты
# raise BaseException, "message" - валидно для 2.х пайтона, не делайте так
# или даже
# raise "message" - валидно для <2.4 пайтона, не делайте так


##################
# Проброс исключений
try:
    raise NameError('Привет Там')
except NameError as exc:
    print(f'Исключение типа {type(exc)} пролетело мимо! его параметры {exc.args}')
    # обратите внимание на "пустой" оператор - будет переброшено исключение текущего скоупа.
    raise
# используется для зачистки возможно порушенных данных и/или логирования ошибки
# и передачи отвественности вовне - пусть там решают что делать дальше

# можно формировать другое исключение
try:
    raise NameError('Привет Там')
except NameError as exc:
    print(f'Поймано исключение типа {type(exc)}')
    raise TypeError('Привет и тут')
# автоматом прицепляется обьект породившего исключения, в атрбибут __cause__

# можно явно указать
try:
    raise NameError('Привет Там')
except NameError as exc:
    print(f'Поймано исключение типа {type(exc)}')
    raise TypeError('Привет и тут') from exc

