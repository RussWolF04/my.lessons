#1. Есть словарь песен группы Depeche Mode
print('Task №_1')
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут
# TODO здесь ваш код
# 1_a
from collections import OrderedDict
singls = OrderedDict({
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
})

# 3 песни группы Depeche Mode (World in My Eyes, Policy of Truth, Blue Dress)
songs_1 = []
songs_1 += (list(singls.items())[0] + list(singls.items())[6] + list(singls.items())[7])
singl_name_1 = [x for x in songs_1[::2]]
long_1 = [i for i in songs_1[1::2]]
print(f'Группа Depeche Mode песни: \n'
      f'1. {singl_name_1[0]} длительность - {long_1[0]}\n'
      f'2. {singl_name_1[1]} длительность - {long_1[1]}\n'
      f'3. {singl_name_1[2]} длительность - {long_1[2]}\n'
      f'Общее звучание этих трех треков = {sum(long_1)}')
print('---------------------------------------------------------------------------------------------------------------')
# 1_b
# Следуюцие 3 песни
songs_2 = (list(singls.items())[1] + list(singls.items())[2] + list(singls.items())[3])
singl_name_2 = [j for j in songs_2[::2]]
long_2 = [k for k in songs_2[1::2]]
print('Песни группы Depeshe Mode')
print(f'1. {singl_name_2[0]} = {long_2[0]} - минуты\n'
      f'2. {singl_name_2[1]} = {long_2[1]} - минуты\n'
      f'3. {singl_name_2[2]} = {long_2[2]} - минуты\n')
print('---------------------------------------------------------------------------------------------------------------')
# 1_c
# Последние 3 песни из словоря задания
songs_3 = (list(singls.items())[4] + list(singls.items())[5] + list(singls.items())[8])
print(songs_3)
singl_name_3 = [a for a in songs_3[::2]]
long_3 = [b for b in songs_3[1::2]]
print('Песни группы Depeshe Mode')
print(f'1. {singl_name_3[0]} = {long_3[0]} - минуты\n'
      f'2. {singl_name_3[1]} = {long_3[1]} - минуты\n'
      f'3. {singl_name_3[2]} = {long_3[2]} - минуты\n')

# Еще один способ
# count = 0
# for i in range(3):
#     count += dict[input('Enter sound: ')]
#     print(round(count, 2))
print('===============================================================================================================')


#2. Есть словарь координат городов
print('Task №_2')
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# TODO здесь заполнение словаря
# city_1 = []
# city_2 = []
# city_1 = sites[input('Enter city: ').title()]
# city_2 = sites[input('Enter city: ').title()]
# distances = ((city_1[0] - city_2[0]) ** 2 + (city_1[1] - city_2[1]) ** 2) ** 0.5
# print(f'Растояние между ними = {distances}')
# print('===============================================================================================================')
len_between = {'Moscow to London': None,
               'Moscow to Paris': None,
               'London to Paris': None,
}
m_l = ((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** (1/2)
l_p = ((sites['London'][0] - sites['Paris'][0]) ** 2 + (sites['London'][1] - sites['Paris'][1]) ** 2) ** (1/2)
m_p = ((sites['Moscow'][0] - sites['Paris'][0]) ** 2 + (sites['Moscow'][1] - sites['Paris'][1]) ** 2) ** (1/2)
len_between['Moscow to London'], len_between['Moscow to Paris'], len_between['London to Paris'] = m_l, m_p, l_p
print(len_between)
print('===============================================================================================================')


#3. Есть словарь кодов товаров
print('Task №_3')
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
tables_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
table_code = goods['Стол']
tables_item = store[table_code][0]
tables_quantity = tables_item['quantity']
tables_price = tables_item['price']
tables_cost = tables_quantity * tables_price
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')
print('---------------------------------------------------------------------------------------------------------------')
tables_item = store[table_code][1]
tables_quantity = tables_item['quantity']
tables_price = tables_item['price']
tables_cost = tables_quantity * tables_price
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')
print('===============================================================================================================')
sofas_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofa_code = goods['Диван']
sofas_item = store[sofa_code][0]
sofas_quantity = sofas_item['quantity']
sofas_price = sofas_item['price']
sofas_cost = sofas_quantity * sofas_price
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')
print('---------------------------------------------------------------------------------------------------------------')
sofas_item = store[sofa_code][1]
sofas_quantity = sofas_item['quantity']
sofas_price = sofas_item['price']
sofas_cost = sofas_quantity * sofas_price
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')
print('===============================================================================================================')
chairs_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chair_code = goods['Стул']
chairs_item = store[chair_code][0]
chairs_quantity = chairs_item['quantity']
chairs_price = chairs_item['price']
chairs_cost = chairs_quantity * chairs_price
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')
print('---------------------------------------------------------------------------------------------------------------')
chairs_item = store[chair_code][1]
chairs_quantity = chairs_item['quantity']
chairs_price = chairs_item['price']
chairs_cost = chairs_quantity * chairs_price
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')
print('---------------------------------------------------------------------------------------------------------------')
chairs_item = store[chair_code][2]
chairs_quantity = chairs_item['quantity']
chairs_price = chairs_item['price']
chairs_cost = chairs_quantity * chairs_price
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')
print('===============================================================================================================')

#3. в саду сорвали цветы
print('Task №_4')
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
print('Garden', garden_set)
print('Meadow', meadow_set)
print('---------------------------------------------------------------------------------------------------------------')
# выведите на консоль все виды цветов
# TODO здесь ваш код
flowers = garden_set.union(meadow_set)
print('Все цветы', flowers)
print('---------------------------------------------------------------------------------------------------------------')
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
everywhere = garden_set & meadow_set
print('Растут в саду и лугу', everywhere)
print('---------------------------------------------------------------------------------------------------------------')
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
onlygarden = garden_set - meadow_set
print('Растут только в саду', onlygarden)
print('---------------------------------------------------------------------------------------------------------------')
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
onlymeadow = meadow_set - garden_set
print('Растут только на лугу', onlymeadow)
print('===============================================================================================================')