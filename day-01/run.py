import sys

def part1(input_data):
    increases = 0
    previous_value = None

    for value in input_data:
        if previous_value and value > previous_value:
            increases += 1

        previous_value = value

    return increases

def part2(input_data):
    increases = 0
    previous_total = None
    index = 0

    while index < len(input_data)-2:
        total = input_data[index] + input_data[index+1] + input_data[index+2]

        if previous_total and total > previous_total:
            increases += 1

        previous_total = total

        index += 1

    return increases

if __name__ == '__main__':
    input_data = [int(num) for num in sys.stdin.read().split('\n') if num]
    print(part1(input_data))
    print(part2(input_data))
