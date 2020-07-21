"""
Miner v.0.1
Игра "Сапер"
Создана по мотивам курса Stepic
"""
a = [int(i) for i in input().split()]
mines = [[1, 1], [2, 2], [3, 2], [4, 4]]
#Генерим игровое поле из 0
field = [[0 for i in range(a[1])] for j in range(a[0])]

#Для каждой мины по ее координатам изменим значение поля на -1
for mine in mines:
    #print(mine[0], mine[1])
    #print(field[mine[0] - 1][mine[1] - 1])
    field[mine[0] - 1][mine[1] - 1] = -1
print(field)

#Поиск ячеек без мин (!= -1)
for line in range(a[0]):
    for column in range(a[1]):
        #print(field[line][column])
        if field[line][column] != -1:
            print('координаты ячейки без мин',line, column)
#Поиск мин в соседних ячейках
            for i in range(-1, 2):
                for j in range(-1, 2):


                    if 0 <= line + i <= a[0] - 1 and 0 <= column + j <= a[1] - 1:
                        print('координаты проверяемой ячейки', line + i, column + j)
                        if field[line + i][column + j] == -1:
                            field[line][column] += 1
print(field)

