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
'''
