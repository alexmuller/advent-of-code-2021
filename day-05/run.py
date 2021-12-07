import sys

from lib.helpers import parse_input, empty_matrix

def populate_straight_lines(matrix, input_data):
    for coords in input_data:
        start_x, start_y = coords[0]
        end_x, end_y = coords[1]

        matrix[start_y][start_x] += 1
        matrix[end_y][end_x] += 1

        if start_y > end_y:
            step_start = start_y-1
            while step_start > end_y:
                matrix[step_start][start_x] += 1
                step_start -= 1
        elif start_y < end_y:
            step_start = start_y+1
            while step_start < end_y:
                matrix[step_start][start_x] += 1
                step_start += 1
        elif start_x > end_x:
            step_start = start_x-1
            while step_start > end_x:
                matrix[start_y][step_start] += 1
                step_start -= 1
        elif start_x < end_x:
            step_start = start_x+1
            while step_start < end_x:
                matrix[start_y][step_start] += 1
                step_start += 1

    return matrix

def populate_diagonal_lines(matrix, input_data):
    for coords in input_data:
        start_x, start_y = coords[0]
        end_x, end_y = coords[1]

        matrix[start_y][start_x] += 1
        matrix[end_y][end_x] += 1

        if end_x > start_x and end_y > start_y:
            next_x = start_x + 1
            next_y = start_y + 1
            while next_y < end_y:
                matrix[next_y][next_x] += 1
                next_x += 1
                next_y += 1
        elif end_x > start_x and end_y < start_y:
            next_x = start_x + 1
            next_y = start_y - 1
            while next_y > end_y:
                matrix[next_y][next_x] += 1
                next_x += 1
                next_y -= 1
        elif start_x > end_x and end_y < start_y:
            next_x = start_x - 1
            next_y = start_y - 1
            while next_y > end_y:
                matrix[next_y][next_x] += 1
                next_x -= 1
                next_y -= 1
        elif start_x > end_x and end_y > start_y:
            next_x = start_x - 1
            next_y = start_y + 1
            while next_y < end_y:
                matrix[next_y][next_x] += 1
                next_x -= 1
                next_y += 1

    return matrix

def part1(input_data):
    matrix = empty_matrix(input_data)
    matrix = populate_straight_lines(matrix, input_data['straight_lines'])

    cells = [cell for row in matrix for cell in row if cell >= 2]

    return len(cells)

def part2(input_data):
    matrix = empty_matrix(input_data)
    matrix = populate_straight_lines(matrix, input_data['straight_lines'])
    matrix = populate_diagonal_lines(matrix, input_data['diagonal_lines'])

    cells = [cell for row in matrix for cell in row if cell >= 2]

    return len(cells)

if __name__ == '__main__':
    text_input = sys.stdin.read()
    print(part1(parse_input(text_input)))
    print(part2(parse_input(text_input)))
