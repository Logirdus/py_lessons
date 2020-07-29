'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана
следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по
этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по
всем абитуриентам.

Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''
import os


def average(ratings):
    '''
    функция вычисления среднего значения переданного списка
    :param ratings: список
    :return: float - среднее значение
    '''
    return(sum(int(i) for i in ratings)/ len(ratings))

def overall_rating(base):
    '''
    функция сбора оценок по предметам для потока
    :param base: словарь с оценками всех учеников
    :return: средние балы по предметам
    '''
    mat, phis, lang = [], [], []
    for key in base:
        mat.append(base[key][0])
        phis.append(base[key][1])
        lang.append(base[key][2])
    return average(mat), average(phis), average(lang)



#Создаем пустую базу абитуриентов
base = {}
mat, phis, rus = [], [], []
with open('input.txt', 'r') as inf, open('output.txt', 'w') as ouf:
#Заполняем базу значениями из файла input.txt
    for line in inf:
        line = line.strip().split(';')
        for i in line:
            base[line[0]] = [line[1], line[2], line[3]]
        mat.append(line[1])
        phis.append(line[2])
        rus.append(line[3])
#Считаем средние балы для каждого абитуриента
    for key, value in base.items():
        print(average(value))

#Собираем все оценки по предметам для потока
for i in [mat, phis, rus]:
    print(average(i), end=' ')
