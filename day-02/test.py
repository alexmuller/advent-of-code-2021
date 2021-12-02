from run import part1, part2

input = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]

solution = part1(input)
assert solution == 150, f'Expected part1 to be 150, got {solution}'

solution = part2(input)
assert solution == 900, f'Expected part1 to be 5, got {solution}'
