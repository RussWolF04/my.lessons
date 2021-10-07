# -*- coding: utf-8 -*-

# Есть архив с книгами(books.rar), необходимо сделать программу помощник читателя.
# Программа должна принять от пользователя слово или некоторое количество слов,
# в ответ программа должна выдать все названия книг в тексте которых есть все введенные пользователем слова.

# TODO здесь ваш код
import requests
import json
import re

# r = requests.get('http://httpbin.org/get')
# print(r.text)

# r = requests.post('http://httpbin.org/post')
# print(r.text)

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.put('http://httpbin.org/get', params=payload)
# print(r.text)

# r = requests.put('http://httpbin.org/put', data={'key': 'value'})
# print(r.text)

# url = 'http://httpbin.org/post'
# r = requests.post(url, data=json.dumps({'key': 'value'}))
# r = requests.post(url, json={'key': 'value'})
# print(r.text)

# r = requests.get('http://httpbin.org/get')
# print(type(r.text), r.text)
# print(type(r.content), r.content)
# print(type(r.json()), r.json())
# print(r.status_code)
# print(r.status_code == requests.codes.ok)

# print('Вызов ОШИБКИ 404')
# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)
# bad_r.raise_for_status()

# print('Обращение на http://github.com')
# r = requests.get('http://github.com')
# print(r.url)
# print(r.status_code)
# print(r.history)

# print('''Если нам не нужно такое поведение,
# нужно запретить перенаправление
# ''')
# r = requests.get('http://github.com', allow_redirects=False)
# print(r.status_code)
# print(r.history)

# print('Курс euro на сегодня 68.7534, курс euro на завтра 67.8714')
# html = 'Курс euro на сегодня 68.7534, курс euro на завтра 67.8714'
# math = re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE).group(1)
# rate = math.group(1)
# rate

import requests
import re

# resp = requests.get('https://www.wikipedia.org')
# html = resp.text
# #
# re_links = re.findall(r'<a[^>] + class="[^"] * other-project-link[^>] + href="([^"]+)', html)
# print(re_links)
# #
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# bs_links = soup('a', 'other-project-link')
# bs_hrefs = [link['href'] for link in bs_links]
# print(bs_hrefs)
#
# from bs4 import BeautifulSoup
# import requests as req
#
# resp = req.get("http://www.something.com")
#
# soup = BeautifulSoup(resp.text, 'lxml')
#
# print(soup.title)
# print(soup.title.text)
# print(soup.title.parent)
#
# from bs4 import BeautifulSoup
# import requests as req
#
# resp = req.get("http://www.something.com")
# soup = BeautifulSoup(resp.text, 'lxml')
# print(soup.prettify())
#
from bs4 import BeautifulSoup
#
with open("http://www.wikipedia.org") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    # print(soup.find("ul", attrs={ "id" : "mylist"}))
    print(soup.find("ul", id="mylist"))

