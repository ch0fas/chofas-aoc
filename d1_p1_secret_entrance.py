# Advent of Code - Day 1, Part 1
# Link: https://adventofcode.com/2025/day/1

dial = 50 # The starting point for the dial
counter = 0 # The amount of times the counter has landed back at 0

example_input = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

with open('data/secret_entrance_input.txt', 'r') as f: #Reading the data
    lines = f.readlines()

lines = [i.strip() for i in lines] # Removing extra spaces

for i in lines:
    #print(i)
    direction = i[0]
    number = int(i[1:])

    # Adding or subtracting depending on direction
    if direction == 'L':
        dial = dial - number
    elif direction == 'R':
        dial = dial + number
    
    # Calculating overflows - using remainder to account for the number being very large
    if dial > 99:
        dial = dial % 100
    elif dial < 0:
        dial = (dial % 100)
    
    print(dial)
    
    if dial == 0:
        counter += 1

print(f'\n Final counter: {counter}') # FINAL ANSWER -> 1078
