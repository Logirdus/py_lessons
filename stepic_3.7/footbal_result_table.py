"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n n n — количество завершенных игр.
После этого идет n n n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

results_table = {'Локомотив':{games:2, win:2, draw:0, defeat:0, score:6}, 'Спартак':{}}

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""


def check_table(teams):
    # функция добавления новых команд в базу
    for team_name in teams:
        if team_name not in results_table:
            results_table[team_name] = {'games': 0, 'win': 0, 'draw': 0, 'defeat': 0, 'score': 0}


def update_table(listing):
    if int(listing[1]) > int(listing[3]):
        results_table[listing[0]]['games']  += 1
        results_table[listing[0]]['win']    += 1
        results_table[listing[0]]['score']  += 3
        results_table[listing[2]]['games']  += 1
        results_table[listing[2]]['defeat'] += 1
    elif int(listing[3]) > int(listing[1]):
        results_table[listing[2]]['games']  += 1
        results_table[listing[2]]['win']    += 1
        results_table[listing[2]]['score']  += 3
        results_table[listing[0]]['games']  += 1
        results_table[listing[0]]['defeat'] +=1
    else:
        results_table[listing[0]]['games'] += 1
        results_table[listing[0]]['score'] += 1
        results_table[listing[0]]['draw']  += 1
        results_table[listing[2]]['games'] += 1
        results_table[listing[2]]['score'] += 1
        results_table[listing[2]]['draw']  += 1


match_count = int(input())
results_table = {}
for i in range(match_count):
    d = input().split(';')
    check_table([d[0], d[2]])
    update_table(d)

for team, result in results_table.items():
    print(team, end=':')
    for value in result.values():
        print(value, end=' ')
    print()