# Advent of Code - Day 2, Part 2
# Link: https://adventofcode.com/2025/day/2

example_nums = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
mini_nums = '11-22,95-115,998-1012'
puzzle_input = '78847-119454,636-933,7143759788-7143793713,9960235-10043487,44480-68595,23468-43311,89-123,785189-1014654,3829443354-3829647366,647009-692765,2-20,30-42,120909-197026,5477469-5677783,9191900808-9191943802,1045643-1169377,46347154-46441299,2349460-2379599,719196-779497,483556-641804,265244-450847,210541-230207,195-275,75702340-75883143,58-84,2152-3237,3367-5895,1552-2029,9575-13844,6048-8966,419388311-419470147,936-1409,9292901468-9292987321'

invalid_ids = 0

def find_factors(n: int) -> list:
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    
    factors.pop(0)

    return factors


# ranges_example = [list(map(int, i.split('-'))) for i in example_nums.split(',')]
# print(ranges_example)

# ranges_mini_example = [list(map(int, i.split('-'))) for i in mini_nums.split(',')]
# print(ranges_mini_example)

ranges_input = [list(map(int, i.split('-'))) for i in puzzle_input.split(',')]

for i in ranges_input:
    print(i)
    for j in range(i[0], i[1]+1):
        stringed_num = str(j)
        for k in find_factors(len(stringed_num)):
            if k == len(stringed_num):
                split_parts = [stringed_num[n] for n in range(0,k)]
                all_same_qm = all(x == split_parts[0] for x in split_parts)
            else:
                split_parts = list(map(''.join, zip(*[iter(stringed_num)]*k)))
                all_same_qm = all(x == split_parts[0] for x in split_parts)

            if all_same_qm == True:
                invalid_ids += j
                break
    
print(f'All invalid ids: {invalid_ids}') # FINAL ANSWER -> 36037497037