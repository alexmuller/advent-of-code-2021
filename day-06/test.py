from run import parse_input, part1, part2

input = '3,4,3,1,2'

solution = part1(parse_input(input))
assert solution == 5934, f'Expected part1 to be 5934, got {solution}'

solution = part2(parse_input(input))
assert solution == 26984457539, f'Expected part2 to be 26984457539, got {solution}'
