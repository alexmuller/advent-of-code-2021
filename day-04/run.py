import sys

from lib.helpers import Board

def parse_input(input_string):
    boards = []
    index = 2

    while True:
        board = input_string.strip().split('\n')[index:index+5]
        boards.append(board)
        index += 6

        if board == []:
            break

    boards = [Board(board) for board in boards if board]

    return {
        'calls': [int(call) for call in input_string.split('\n')[0].split(',') if call],
        'boards': boards,
    }

def part1(input_data):
    for call in input_data['calls']:
        for board in input_data['boards']:
            res = board.new_call(call)
            if res:
                return res

    raise Exception('No winners')

def part2(input_data):
    for call in input_data['calls']:
        remaining_boards = [board for board in input_data['boards'] if board.is_complete == False]

        for board in remaining_boards:
            res = board.new_call(call)

            if len(remaining_boards) == 1 and res:
                return call * board.unmarked_sum()

    raise Exception('No winners')

if __name__ == '__main__':
    text_input = sys.stdin.read()
    print(part1(parse_input(text_input)))
    print(part2(parse_input(text_input)))
