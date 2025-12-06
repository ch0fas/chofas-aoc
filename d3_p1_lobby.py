# Advent of Code - Day 3, Part 1
# Link: https://adventofcode.com/2025/day/3

example_input = ['987654321111111','811111111111119','234234234234278','818181911112111']

with open('data/lobby_input.txt','r') as f:
    lines = f.readlines()

total_joltage = 0

for i in lines:
    joltages = []
    for j in range(len(i)):
        front_values = i[j+1:]
        for k in range(len(front_values)):
            stringed_num = i[j] + front_values[k]
            joltages.append(int(stringed_num))
    
    total_joltage += max(joltages)
    
print(f'Total Joltage: {total_joltage}') # FINAL ANSWER -> 17092