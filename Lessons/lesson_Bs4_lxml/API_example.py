import requests
from bs4 import BeautifulSoup

# resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
# soup = BeautifulSoup(resp.content, "xml")
# print(soup)

# print(soup.find('CharCode', text='EUR').find_next_sibling('Value').string)

# print(soup.find(ID="R01239").Value.string)


# resp = requests.get(
#     "http://api.openweathermap.org/data/2.5/weather",
#     params={
#         "q": "Moscow",
#         "APPID": "a4ca581bf1870a4c2e39d02980695d94",
#         'mode': 'xml', 'units': 'metric'
# } )
#
# soup = BeautifulSoup(resp.content, "xml")
# print(soup.temperature['value'])

# import requests
# resp = requests.get(
#     "http://api.openweathermap.org/data/2.5/weather",
#     params={
#         "q": "Moscow",
#         "APPID": "a4ca581bf1870a4c2e39d02980695d94",
#         'mode': 'json', 'units': 'metric'
# } )
# data = resp.json()
# print(data['main']['temp'])

# import requests
#
# resp = requests.get(
#     'https://api.vk.com/method/users.get',
#     params={'user_id': '1'}
# )
# print(resp.json())


# import vk
#
# session = vk.Session(
#     access_token='3d6902af41bbae31cb6de95061f8ffb02448ecad51cafd59ffce82313948327de68a3b80471ce2f999d60',
# )
# api = vk.API(session)
# print(api.users.get(user_ids=1, v=5.131))
