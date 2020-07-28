d=[]
with open('input2.txt', 'r') as input_file:
    for line in input_file:
        line = line.strip()
        words = [i for i in line.lower().split()]
        for word in words:
            d.append(word)
    d.sort()
    print(d)
    print(d.count('abv'))
    maxd = d[0]
    i = 0
    while i < len(d) - 1:
        i += 1
        if d[i] == maxd:
            continue
        else:
            if d.count(maxd) < d.count(d[i]):
                maxd = d[i]
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
