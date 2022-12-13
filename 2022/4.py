with open('Data/4.txt') as fin:
    input = list(map(tuple, list(line.split(',') for line in fin.read().rstrip().split('\n'))))

cleaning_rota = []

for item in input:
    cleaning_rota.extend([[(int(item[0].split('-')[0]), int(item[0].split('-')[1])), (int(item[1].split('-')[0]), int(item[1].split('-')[1]))]]) 

completely_overlapping_pairs = 0

for pair in cleaning_rota:
    completely_overlapping_pairs += (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1])

overlapping_pairs = 0

for pair in cleaning_rota:
    if max(pair[0]) >= min(pair[1]) and not min(pair[0]) > max(pair[1]):
        overlapping_pairs += 1

print(overlapping_pairs)
