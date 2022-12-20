def openfile():
    with open('Data/5.txt') as fin:
        input = fin.read()
    return input

stack = {
    1 : ['W', 'D', 'G', 'B', 'H', 'R', 'V'],
    2 : ['J', 'N', 'G', 'C', 'R', 'F'],
    3 : ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
    4: ['J', 'D', 'S', 'V'],
    5: ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
    6: ['P', 'G', 'H', 'C', 'M'],
    7: ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
    8: ['S', 'J', 'R'],
    9: ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']
}

REPLACEMENTS =[
    (' from ', ','),
    (' to ', ','),
    ('move ', '')
]

def create_instructions(REPLACEMENTS):
    input = openfile()

    for old, new in REPLACEMENTS:
        input = input.replace(old, new)

    input = list(input.split('\n'))
    input = input[10:-1]
    instructions =[]
    for item in input:
        item = item.split(',')
        item = list(map(int, item))
        instructions.append(item)
    return instructions

instructions = create_instructions(REPLACEMENTS)

def rearrange_stack(stack, instructions):

    #for line in instructions:
    #    count = line[0]
    #    crane = []
    #    while count > 0:    
    #        crane.append(stack[line[1]].pop())
    #        count -= 1
    #    stack[line[2]].extend(crane)

    for line in instructions:
        pivot = len(stack[line[1]]) - line[0]
        crane = []
        crane.extend(stack[line[1]])
        del stack[line[1]][pivot:]
        del crane[:pivot]
        stack[line[2]].extend(crane)

    string_code = ""
    for i in range(1, 10):
        string_code += stack[i][-1]

    return string_code

print(rearrange_stack(stack, instructions))