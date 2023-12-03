def open_file(path):
    with open(path) as fin:
        input = fin.read().split('\n')
    return [line for line in input if line]

CUBES_IN_BAG = {
    'red': 12,
    'green': 13,
    'blue': 14
}

data = open_file('data/2.txt')
total = 0
power = 0

for game in data:
    power_for_game = 1
    cubes_out_of_bag = {}
    title, game = game.split(':')
    id = int(title.lstrip('Game '))
    sets = game.split(';')
    for hand in sets:
        for cubes in hand.split(','):
            colour = ''.join(letter for letter in cubes if letter.isalpha())
            number_of_balls = int(''.join(letter for letter in cubes if letter.isdigit()))
            if colour in cubes_out_of_bag.keys():
                if number_of_balls > cubes_out_of_bag[colour]:
                    cubes_out_of_bag[colour] = number_of_balls
            else:
                cubes_out_of_bag[colour] = number_of_balls
            if number_of_balls > CUBES_IN_BAG[colour]:
                id = 0
    for minimum in cubes_out_of_bag.values():
        power_for_game *= minimum
    power += power_for_game
    total += id
         
print(total)
print(power)