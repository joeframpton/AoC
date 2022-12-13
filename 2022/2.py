fin = open('Data/2.txt')
input = fin.read().replace(" ","").split("\n")
fin.close
my_hand = {
    "X" : 1,
    "Y" : 2, 
    "Z" : 3,
}
result = {
    "AX" : 3,
    "BY" : 3,
    "CZ" : 3,
    "AY" : 6,
    "BZ" : 6,
    "CX" : 6,
    "AZ" : 0,
    "BX" : 0,
    "CY" : 0
}
#AX BY CZ == 3
#AY BZ CX == 6
#AZ BX CY == 0

# X Loss
# Y Draw
# Z Win
result_2 = {
    "AX" : 0 + 3, #Rock Loss
    "BY" : 3 + 2, #Paper Draw
    "CZ" : 6 + 1, #Sci Win
    "AY" : 3 + 1, # Rock Draw
    "BZ" : 6 + 3, #Paper Win
    "CX" : 0 + 2, #Sci Loss
    "AZ" : 6 + 2, #Rock Win
    "BX" : 0 + 1, #Paper Loss
    "CY" : 3 + 3 #Sci Draw
}

total = 0
for round in input:
    total += my_hand[round[1]]
    total += result[round]

print(total)

total_2 = 0

for round in input:
    total_2 += result_2[round]

print(total_2)

    

        
    