def openfile():
    with open('Data/6.txt') as fin:
        input = fin.read()
    return input

input = openfile()

def marker(input):
    for i, char in enumerate(input):
        if i < 14:
            continue
        #buffer = input[i-4:i]
        buffer = input[i-14:i]
        if len(set(buffer)) == len(buffer):
            return i
    return "There has been an error"    