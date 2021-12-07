def parse_input(input_string):
    list_of_lines = input_string.strip().split('\n')
    list_of_lines = [[tuple(map(int, y.split(','))) for y in x.split(' -> ')] for x in list_of_lines]

    straight_lines = [line for line in list_of_lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]
    diagonal_lines = [line for line in list_of_lines if line[0][0] != line[1][0] and line[0][1] != line[1][1]]

    return {
        'straight_lines': straight_lines,
        'diagonal_lines': diagonal_lines,
    }

def empty_matrix(input_data):
    max_x = max([item[0] for sublist in input_data['straight_lines'] for item in sublist])
    max_y = max([item[1] for sublist in input_data['straight_lines'] for item in sublist])

    matrix = []
    for y in range(max_y+1):
        matrix.append([0] * (max_x + 1))

    return matrix

def print_matrix(matrix):
    print('')
    for row in matrix:
        print(' '.join([str(cell) for cell in row]))
    print('- - -')
