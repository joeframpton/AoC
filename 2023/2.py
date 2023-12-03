data = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'.split('\n')

def open_file(path):
    with open(path) as fin:
        input = fin.read().split('\n')
    return [line for line in input if line]

CUBES_IN_BAG = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def game_is_possible(cubes_out_of_bag, cubes_in_bag=CUBES_IN_BAG):
    for colour in cubes_out_of_bag.keys():
        if cubes_out_of_bag[colour] > cubes_in_bag[colour]:
            return False
    return True


data = open_file('data/2.txt')
#print(data)

total = 0

for game in data:
    cubes_out_of_bag = {}
    title, game = game.split(':')
    id = int(title.lstrip('Game '))
    sets = game.split(';')
    for hand in sets:
        for cubes in hand.split(','):
            colour = ''.join(letter for letter in cubes if letter.isalpha())
            number_of_balls = int(''.join(letter for letter in cubes if letter.isdigit()))
            if number_of_balls > CUBES_IN_BAG[colour]:
                id = 0
    total += id
print(total)          
    