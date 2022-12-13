def calorie_counter():    
    fin = open("data/input.txt")
    calories_strings = fin.read().split("\n")
    fin.close()
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