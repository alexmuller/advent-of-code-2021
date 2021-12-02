import sys

def part1(input_data):
    horizontal = 0
    depth = 0

    for command in input_data:
        direction, number = command.split(' ')
        if direction == 'forward':
            horizontal += int(number)
        elif direction == 'down':
            depth += int(number)
        elif direction == 'up':
            depth -= int(number)
        else:
            raise Exception

    return (horizontal * depth)

def part2(input_data):
    horizontal = 0
    depth = 0
    aim = 0

    for command in input_data:
        direction, number = command.split(' ')
        if direction == 'forward':
            horizontal += int(number)
            depth += aim * int(number)
        elif direction == 'down':
            aim += int(number)
        elif direction == 'up':
            aim -= int(number)
        else:
            raise Exception

    return (horizontal * depth)

if __name__ == '__main__':
    input_data = [command for command in sys.stdin.read().split('\n') if command]
    print(part1(input_data))
    print(part2(input_data))
