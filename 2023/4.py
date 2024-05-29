def open_file(path):
    with open(path) as fin:
        input = fin.read().split('\n')
    return [line for line in input if line]

raw_data = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n\
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n\
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

## answer is 8, 2, 2, 1, 0, 0 TOTAL = 13


data = [line for line in raw_data.split('\n')]

data = open_file('data/4.txt')

ordered_data = dict()
score = 0

for line in data:
    res = line.split(':')
    nums_strings = res[1].split('|')
    winning_numbers = [int(num) for num in nums_strings[0].split(' ') if num.isdigit()]
    my_numbers = [int(num) for num in nums_strings[1].split(' ') if num.isdigit()]
    card_number = int(''.join([char for char in res[0] if char.isdigit()]))
    ordered_data[card_number] = [winning_numbers, my_numbers, 1]
    
for card, numbers in ordered_data.items():
    card_score = 0
    for winning_number in numbers[0]:
        if winning_number in numbers[1]:
            card_score = card_score * 2 if card_score > 0 else 1
    score += card_score
print('Part 1 Score: ', score)

total_cards = 0
for card, numbers in ordered_data.items():
    card_score = 0
    current_card = card
    for winning_number in numbers[0]:
        if winning_number in numbers[1]:
            card_score += 1

    for card_number in range(card + 1, card + 1 + card_score):
        if card_number in ordered_data:
            ordered_data[card_number][2] += numbers[2]
    total_cards += numbers[2]
print('Part 2 Score: ', total_cards)

# 9963 Too low
        
        
    
            


        

