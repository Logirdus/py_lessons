"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
"""
import requests

with open('chainlink.txt', 'r') as starturl:
    url = starturl.readline().strip()
    content = requests.get(url).text
    while content[:2] != 'We':
        content = requests.get(url).text
        url = 'https://stepic.org/media/attachments/course67/3.6.3/' + content
with open('chainanswer.txt', 'w') as ans:
    ans.write(content)