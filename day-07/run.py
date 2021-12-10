def parse_input(text_input):
    return [int(position) for position in text_input.split(',')]

def candidate_positions(data):
    minimum = min(data)
    maximum = max(data)
    return range(minimum, maximum+1)

def part1(data):
    candidates = candidate_positions(data)
    positions = {}

    for candidate in candidates:
        fuel = [abs(submarine - candidate) for submarine in data]
        positions[candidate] = sum(fuel)

    return min(positions.values())

def part2(data):
    candidates = candidate_positions(data)
    positions = {}

    for candidate in candidates:
        fuels = [abs(submarine - candidate) for submarine in data]
        adjusted_fuel = [(0.5 * fuel * (fuel + 1)) for fuel in fuels]
        positions[candidate] = sum(adjusted_fuel)

    return int(min(positions.values()))
