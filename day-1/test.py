from run import part1, part2

input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

solution = part1(input)
assert solution == 7, f'Expected part1 to be 7, got {solution}'

solution = part2(input)
assert solution == 5, f'Expected part1 to be 5, got {solution}'
