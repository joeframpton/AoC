with open('Data/6.txt') as fin:
    input = fin.read()

def marker(input):
    for i, char in enumerate(input):
        if i < 14:
            continue
        #x = input[i-4:i]
        x = input[i-14:i]
        if len(set(x)) == len(x):
            return i
    return "There has been an error"    

print(marker(input))
