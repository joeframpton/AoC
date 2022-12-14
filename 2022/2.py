def open_file(file_location):
    with open(file_location) as fin:
        input = fin.read().replace(' ','').split('\n')
    return input

input = open_file('Data/2.txt')

MY_HAND = {
    'X' : 1,
    'Y' : 2, 
    'Z' : 3,
}
RESULT = {
    'AX' : 3,
    'BY' : 3,
    'CZ' : 3,
    'AY' : 6,
    'BZ' : 6,
    'CX' : 6,
    'AZ' : 0,
    'BX' : 0,
    'CY' : 0
}

#AX BY CZ == 3
#AY BZ CX == 6
#AZ BX CY == 0

# X Loss
# Y Draw
# Z Win

RESULT_2 = {
    'AX' : 0 + 3, #Rock Loss
    'BY' : 3 + 2, #Paper Draw
    'CZ' : 6 + 1, #Sci Win
    'AY' : 3 + 1, # Rock Draw
    'BZ' : 6 + 3, #Paper Win
    'CX' : 0 + 2, #Sci Loss
    'AZ' : 6 + 2, #Rock Win
    'BX' : 0 + 1, #Paper Loss
    'CY' : 3 + 3 #Sci Draw
}

def RPS(input, MY_HAND, RESULT):
    total = 0
    for round in input:
        total += MY_HAND[round[1]]
        total += RESULT[round]
    return(total)

def RPS_2(input, RESULT_2):
    total = 0
    for round in input:
        total += RESULT_2[round]
    return total
