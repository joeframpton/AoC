import re

#text = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet".split()
text = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen".split()

def open_file(path):
    with open(path) as fin:
        input = fin.read().split('\n')
    return [line for line in input if line]


### Overcooked it thinking an edgecase of eightwo should end up as 8wo, it's actually 28 https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
# def replace_num(dictionary, string):
#     indexes = {str(i):k for k,i in {key: string.find(key) for key in dictionary.keys()}.items() if i > -1}
#     if len(indexes) == 0:
#         return string
#     else: 
#         min_index = min(indexes.keys())
#         string = string.replace(indexes[min_index], conversion[indexes[min_index]])
#         string = replace_num(dictionary, string)
#     return string

def string_to_nums(string):
    #index, number
    indexes = {str(i):k for k,i in {num: string.find(word) for word, num in conversion.items()}.items() if i > -1}
    ##lazily trying from the right in case of multiples...
    indexes.update({str(i):k for k,i in {num: string.rfind(word) for word, num in conversion.items()}.items() if i > -1})

    #index, number
    indexes_digits = {str(i) : letter for i, letter in enumerate(string) if letter.isdigit()}
    indexes.update(indexes_digits)
    if len(indexes.keys()) < 2:
        first_num = indexes[min(indexes.keys())]
        last_num = indexes[max(indexes.keys())]

    first_num = indexes[str(min(list(int(k) for k in indexes.keys())))]
    last_num = indexes[str(max(list(int(k) for k in indexes.keys())))]
    return int(first_num + last_num)

conversion = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5', 
    "six": '6', 
    "seven": '7',
    "eight": '8',
    "nine": '9',
}
text = open_file('data/1.txt')

total = 0

for line in text:
    num = string_to_nums(line)
    total += num

print(total)
