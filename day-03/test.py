from lib.helpers import gamma, epsilon, binary_to_decimal
from run import part1, part2

input = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

gamma_value = gamma(input)
assert gamma_value == '10110', f'Expected gamma to be 10110, got {gamma_value}'

epsilon_value = epsilon(input)
assert epsilon_value == '01001', f'Expected epsilon to be 01001, got {epsilon_value}'

decimal = binary_to_decimal('10110')
assert decimal == 22, f'Expected decimal to be 22, got {decimal}'

decimal = binary_to_decimal('01001')
assert decimal == 9, f'Expected decimal to be 9, got {decimal}'

solution = part1(input)
assert solution == 198, f'Expected part1 to be 198, got {solution}'

solution = part2(input)
assert solution == 230, f'Expected part2 to be 230, got {solution}'
