# import requests
# import re

# resp = requests.get('https://www.wikipedia.org')
# html = resp.text
# re_links = re.findall(r'<a[^>]+class="[^"]*other-project-link[^>]+href="([^"]+)',
#                       html)
# print(re_links)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# bs_links = soup('a', 'other-project-link')
# bs_hrefs = [link['href'] for link in bs_links]
# print(bs_hrefs)

# html = """<!DOCTYPE html>
# <html lang="en">
#   <head>
#     <title>test page</title>
#   </head>
#   <body class="mybody" id="js-body">
#     <p class="text odd">first <b>bold</b> paragraph</p>
#     <p class="text even">second <a href="https://mail.ru">link</a></p>
#     <p class="list odd">third <a id="paragraph"><b>bold link</b></a></p>
#   </body>
# </html>
# """
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(html, 'lxml')
# print(soup)
#
# print(soup.p.b.string)
# print(type(soup.p.b.string))
#
# print(soup.p['class'])
#
# print(soup.p.parent.name)
#
# print([i.name for i in soup.p.b.parents])
#
# print(soup.p.next)
#
# print(soup.p.next_sibling)
#
# print(soup.p.contents)
#
# print(soup.p.children)
# print(list(soup.p.children))

# html = """<!DOCTYPE html>
# <html lang="en">
#   <head>
#     <title>test page</title>
#   </head>
#   <body class="mybody" id="js-body">
#     <p class="text odd">first <b>bold</b> paragraph</p>
#     <p class="text even">second <a href="https://mail.ru">link</a></p>
#     <p class="list odd">third <a id="paragraph"><b>bold link</b></a></p>
#   </body>
# </html>
# """
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(html, "lxml")

# print(soup.p.b.find_parent("body")["id"])

# print(soup.p.find_next_sibling(class_="odd"))

# print(list(soup.p.next_siblings))


# print(soup.p.find('b'))
# print(soup.find(id='js-body')['class'])
# print(soup.find('b', text='bold'))

# print(soup.find_all('p'))

# print(soup.find_all('p', 'text odd'))

# print(soup.select('p.odd.text'))

# print(soup.select("p:nth-of-type(3)"))

# print(soup.select("a > b"))

# import re
#
# print([i.name for i in soup.find_all(name=re.compile('^b'))])
#
# print([i for i in soup(['a', 'b'])])
#
# tag = soup.b
# print(tag)
# tag.name = 'i'
# tag['id'] = 'myid'
# tag.string = 'italic'
# print(soup.p)

# import requests
#
# result = requests.get("https://news.mail.ru/")
# soup = BeautifulSoup(result.content, "lxml")
# soup = [
#     (
#         section.string,
#         [
#             header.string for header in section.find_parents()[4].find_all(
#             class_=['newsitem__title-inner', 'link__text', 'collections__title', 'photo__title']
#         )
#         ]
#     ) for section in soup(class_='hdr__inner')]
# print(soup)
