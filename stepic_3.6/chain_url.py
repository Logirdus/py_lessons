"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""
import requests

with open('chainlink.txt', 'r') as chainlink:
    url = chainlink.readline().strip()
answer = '    '
while answer != 'We':

    answer = requests.get(url).text[:2]
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + requests.get(url).text
else: print(requests.get(url).text)