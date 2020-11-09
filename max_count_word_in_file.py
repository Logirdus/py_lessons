d=[]
with open('input2.txt', 'r') as input_file:
    for line in input_file:
        line = line.strip()
        words = [i for i in line.lower().split()]
        for word in words:
            d.append(word)
maxd = d[0]
for word in sorted(set(d)):
    if d.count(word) > d.count(maxd):
        maxd = word
print(maxd, d.count(maxd))


'''
взять первый элемент списка
взять его количество и принять за макс
если элемент не последний
    сравнить взятый элемент со следующим
    если они одинаковы, continue
    если не одинаковы
    сравнить их количество - взять за макс
Оптимизировано:
    Делаем список  уникальных значений из исходного списка set(d)
    Чтобы получить сортированный список делаем sorted(set(d))
    признаем самым частым первое значение списка
    Для каждого значения из set считаем его количество в исходном списке d
    если количество больше, чем у первого - берем его за самый частый
'''
