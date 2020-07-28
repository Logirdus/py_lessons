numbers = ['0','1','2','3','4','5','6','7','8','9']
count = ''
#print(count + str(3))
def counting(): pass

restored = open('restored_file.txt', 'w')

with open('text.txt', 'r') as quiz:
    for line in quiz:
        alfa = line[0]
        for i in range(1, len(line)):
            if line[i] not in numbers or i+1 > len(line):
                print(alfa * int(count), end='')
                restored.write(alfa * int(count))
                alfa = line[i]
                count = ''
            else:
                count += str(line[i])
        restored.write(alfa * int(count))
        print(alfa * int(count), end='')
            #print(line[i])


restored.close()