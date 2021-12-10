import sys

from lib.helpers import parse_input

def bad_tick(fishes):
    new_fishes = []
    number_of_babies = 0

    for fish in fishes:
        timer = fish-1

        if timer < 0:
            timer = 6
            number_of_babies += 1

        new_fishes.append(timer)

    for baby in range(number_of_babies):
        new_fishes.append(8)

    return new_fishes

def good_tick(fishes):
    new_fishes = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6]
    fishes[6] = fishes[7] + new_fishes
    fishes[7] = fishes[8]
    fishes[8] = new_fishes

    return fishes

def part1(fishes):
    after_n_days = 80

    for _ in range(after_n_days):
        fishes = bad_tick(fishes)

    return len(fishes)

def part2(fishes):
    after_n_days = 256

    population_by_timer = {}

    for i in range(9):
        population_by_timer[i] = 0

    for fish in fishes:
        population_by_timer[fish] += 1

    for _ in range(after_n_days):
        good_tick(population_by_timer)

    return sum(population_by_timer.values())

if __name__ == '__main__':
    text_input = sys.stdin.read()
    print(part1(parse_input(text_input)))
    print(part2(parse_input(text_input)))
