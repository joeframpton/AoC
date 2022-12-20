def open_file(file_location):
    with open(file_location) as fin:
        input = fin.read()
    return input

def calorie_counter():    
    input = open_file('data/1.txt')
    calories_strings = input.split('\n')
    calories_lists = []
    counter = []
    for item in calories_strings:
        if item == '':
            calories_lists.append(counter)
            counter = []
            continue
        counter.append(int(item))
    sum_calories = [sum(items) for items in calories_lists]
    sort_calories = sorted(sum_calories)
    top_3 = sort_calories[-1] + sort_calories [-2] + sort_calories [-3]
    return top_3                    

print(calorie_counter())