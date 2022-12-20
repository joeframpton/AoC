def open_file():
    with open('Data/3.txt') as fin:
        input = fin.read().split('\n')
    return input

def prioritisation(item):
    if item.isupper():
        return ord(item) - 38
    elif item.islower():
        return ord(item) - 96

def find_common_items():
    input = open_file()
    filled_rucksacks = []
    for rucksack in input:
        comp_1 = rucksack[:len(rucksack)//2]
        comp_2 = rucksack[len(rucksack)//2:]
        filled_rucksacks.append((comp_1, comp_2))

    common_items = []

    for rucksack in filled_rucksacks:
        common_items_holder = []
        for count, item in enumerate(rucksack[0]):
            if item in rucksack[1] and item not in common_items_holder:
                common_items_holder.append(item)
        common_items.extend(common_items_holder)

    proritised_items = list(map(prioritisation, common_items))
    return proritised_items

def find_badges():
    badges = []
    for index, rucksack in enumerate(input, 1):
        badge_holder = []
        if index % 3 == 0:
            for char in rucksack:
                if char in input[index-2] and char in input[index-3] and char not in badge_holder:
                    badge_holder.append(char)
        badges.extend(badge_holder)

    prioritised_badges = list(map(prioritisation, badges))
    return sum(prioritised_badges)

# I have since learnt about set intersection which would make this much easier...