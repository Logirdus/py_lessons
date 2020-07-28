numbers = ['0','1','2','3','4','5','6','7','8','9']
count = ''
#print(count + str(3))
def counting(): pass

with open('text.txt', 'r') as quiz:
    for line in quiz:
        alfa = line[0]
        for i in range(1, len(line)):
            if line[i] not in numbers or i+1 > len(line):
                print(alfa * int(count), end='')
                alfa = line[i]
                count = ''
            else:
                count += str(line[i])
        print(alfa * int(count), end='')
            #print(line[i])


