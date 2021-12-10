from run import parse_input, part1, part2

input = '16,1,2,0,4,2,7,1,2,14'

solution = part1(parse_input(input))
assert solution == 37, f'Expected part1 to be 37, got {solution}'

solution = part2(parse_input(input))
assert solution == 168, f'Expected part2 to be 168, got {solution}'
