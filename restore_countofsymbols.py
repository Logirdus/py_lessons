numbers = ['0','1','2','3','4','5','6','7','8','9']
count = ''

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        symbol = line[0]
        for i in range(1, len(line)):
            if line[i] not in numbers:
                output_file.write(symbol * int(count))
                symbol = line[i]
                count = ''
            else:
                count += str(line[i])
        output_file.write(symbol * int(count))