# Advent of Code - Day 3, Part 2
# Link: https://adventofcode.com/2025/day/3

from itertools import combinations

example_input = ['987654321111111','811111111111119','234234234234278','818181911112111']

with open('data/lobby_input.txt','r') as f:
    lines = f.readlines()

total_joltage = 0

for i in lines:
    digits = [int(x) for x in i.strip()]
    remaining = 12
    result = []
    start = 0

    while remaining:
        end = len(digits) - remaining

        best_pos = max(range(start, end+1), key=lambda j: digits[j])
        result.append(digits[best_pos])

        start = best_pos + 1
        remaining -= 1
    
    num = 0
    for d in result:
        num = num*10 + d
    
    total_joltage += num
    print('Done')

print(f'Total Joltage: {total_joltage}') # FINAL ANSWER -> 170147128753455