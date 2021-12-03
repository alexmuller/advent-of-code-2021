import collections
import sys

from lib.helpers import gamma, epsilon, binary_to_decimal

def oxygen_generator_rating(input_data):
    num_bits = len(input_data[0])

    for bit_considered in range(num_bits):
        bits = [byte[bit_considered] for byte in input_data]
        counter = collections.Counter(bits)

        if counter['1'] >= counter['0']:
            requested = '1'
        else:
            requested = '0'

        input_data = [value for value in input_data if value[bit_considered] == requested]

        if len(input_data) == 1:
            return input_data[0]

    raise Exception

def co2_scrubber_rating(input_data):
    num_bits = len(input_data[0])

    for bit_considered in range(num_bits):
        bits = [byte[bit_considered] for byte in input_data]
        counter = collections.Counter(bits)

        if counter['1'] < counter['0']:
            requested = '1'
        else:
            requested = '0'

        input_data = [value for value in input_data if value[bit_considered] == requested]

        if len(input_data) == 1:
            return input_data[0]

    raise Exception

def part1(input_data):
    return binary_to_decimal(gamma(input_data)) * binary_to_decimal(epsilon(input_data))

def part2(input_data):
    oxygen_rating = binary_to_decimal(oxygen_generator_rating(input_data))
    co2_rating = binary_to_decimal(co2_scrubber_rating(input_data))
    life_support_rating = oxygen_rating * co2_rating
    return life_support_rating

if __name__ == '__main__':
    input_data = [command for command in sys.stdin.read().split('\n') if command]
    print(part1(input_data))
    print(part2(input_data))
