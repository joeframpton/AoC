def open_file(path):
    with open(path) as fin:
        input = fin.read().split('\n')
    return [line for line in input if line]

data = '467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..'.split('\n')
data = open_file('data/3.txt')

symbols = []
for line in data:
    for letter in line:
        if not letter.isalnum() and letter not in symbols:
            symbols.append(letter)
symbols = [sym for sym in symbols if sym != "."]
#symbols = '#!@*/\%=-<>|?:;[]&^$¬+`'

total = 0
previous_line = []

for line in data:
    number = False
    coded_line = []
    coding_number = {}
    symbol_indeces = []
    for i, letter in enumerate(line):
        if number == False:
            if letter.isdigit():
                number = True
                coding_number['number'] = dict(number = int(letter),
                                               index_start = i,
                                               index_end = i)
                if i == len(line) - 1:
                    coded_line.append(coding_number)
        elif number == True:
            if letter.isdigit():
                coding_number['number']['number'] = int(str(coding_number['number']['number']) + str(letter))
                if i == len(line) - 1:
                    coding_number['number']['index_end'] = i
                    coded_line.append(coding_number)
            else:
                coding_number['number']['index_end'] = i-1
                coded_line.append(coding_number)
                coding_number = {}
                number = False
            
        if letter in symbols:
            number = False
            coded_line.append(dict(symbol = dict(index = i)))
            symbol_indeces.append(i)

    for entry in previous_line:
        if 'symbol' in entry.keys():
            symbol_index = entry['symbol']['index']
            for item in coded_line:
                if 'number' in item.keys():
                    number_index_range = range(item['number']['index_start'] - 1, item['number']['index_end'] + 2)
                    if symbol_index in number_index_range:
                        print(item['number']['number'])
                        total += item['number']['number']
                        #coded_line.remove(item)

    for index in symbol_indeces:
        for item in previous_line:
            if 'number' in item.keys():
                number_index_range = range(item['number']['index_start']-1, item['number']['index_end'] + 2)
                if index in number_index_range:
                    print(item['number']['number'])
                    total += item['number']['number']
                    #previous_line.remove(item)


        for item in coded_line:
            if 'number' in item.keys():
                number_index_range = range(item['number']['index_start'] - 1, item['number']['index_end'] + 2)
                if index in number_index_range:
                    print(item['number']['number'])
                    total += item['number']['number']
                    #coded_line.remove(item)

    previous_line = coded_line
print(total)