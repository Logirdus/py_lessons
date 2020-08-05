n = int(input())
array = [[0 for i in range(n)] for j in range(n)]
print(array)
i = 0
x = 1
for i in range(n):
    for j in range(4, -1, -1):
        array[i][j] = x
        x += 1
        print(array[i][j])
for i in range(n):
    print(array[i])