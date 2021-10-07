# import re
# html = "Курс евро на сегодня 68,7514, курс евро на завтра 67,8901"
# match = re.search(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)
# rate = match.group(1)
# print(rate)
#
# print(re.search(r'Евро.*(\d+,\d+)', html, re.IGNORECASE).group(1))
#
# print(re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE).group(1))
#
# print(re.findall(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE))
#
# print(re.findall(r'Евро\D+\d+,\d+', html, re.IGNORECASE))
#
# print(re.findall(r'Евро\D+(\d+),(\d+)', html, re.IGNORECASE))
#
# print(re.findall(r'Евро\D+((\d+),(\d+))', html, re.IGNORECASE))

# import re
#
# text = '''
# Автомобиль с номером А123ВС77 подрезал автомобиль К654НЕ197, спровоцировав ДТП с участием еще двух иномарок с номерами
# М542ОР777 и О007ОО77
# '''
# pattern = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
# matches = re.findall(pattern, text)
# print(matches)

# import re
#
# nicknames = ['sU3r_h4XX0r', 'alёna', 'ivan ivanovich']
# reg = re.compile(r'\w+')
# for nick in nicknames:
#     print('{} nickname: "{}"'.format(
#         'valid' if reg.match(nick) else 'invalid', nick
#     ))


# import re
#
# nicknames = ['sU3r_h4XX0r', 'alёna', 'ivan ivanovich']
# reg = re.compile(r'^\w+$', re.ASCII)
# for nick in nicknames:
#     print('{} nickname: "{}"'.format(
#         'valid' if reg.match(nick) else 'invalid',
#         nick))


# import re
#
# text = (
#     'Анна и Лена загорали на берегу океана, '
#     'когда к ним подошли Яна и Ильнар'
# )
# print(re.findall(r'[А-Я]\w*на', text))
#
# print(re.findall(r'\b[А-Я]\w*на\b', text))


# import re
#
# text = (
#     'Анна и Елена загорали на берегу океана, '
#     'когда к ним подошли ЯНА, ПОЛИна и Ильнар'
# )
# print(re.findall(r'\b[А-Я]\w*(на|НА)\b', text))
#
# re.findall(r'\b[А-Я]\w*(?:на|НА)\b', text)

