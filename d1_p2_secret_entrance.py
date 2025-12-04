# Advent of Code - Day 1, Part 2
# Link: https://adventofcode.com/2025/day/1

dial = 50 # The starting point for the dial
counter = 0 # The amount of times the counter has landed back at 0

example_input = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

with open('data/secret_entrance_input.txt', 'r') as f: #Reading the data
    lines = [int(line.replace('L','-').replace('R','')) for line in f]

for i in lines:
    if i < 0:
        div, rem = divmod(i, -100)
        counter += div
        if dial != 0 and dial + rem <= 0:
            counter += 1
    
    else:
        div, rem = divmod(i, 100)
        counter += div
        if dial + rem >= 100:
            counter += 1
    
    dial = (dial + i) % 100

print(counter)