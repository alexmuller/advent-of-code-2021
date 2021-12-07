from run import parse_input, part1, part2

input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

solution = part1(parse_input(input))
assert solution == 5, f'Expected part1 to be 5, got {solution}'

solution = part2(parse_input(input))
assert solution == 12, f'Expected part2 to be 12, got {solution}'
