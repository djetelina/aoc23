from itertools import product
from pathlib import Path

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

number_indexes = {}
symbol_indexes = []
gear_indexes = {}
found_numbers = []


def main():
    with open(Path.cwd() / 'inputs' / '3.txt', 'r') as f:
        puzzle_input = f.readlines()
    puzzle_matrix = [[c for c in line.strip()] for line in puzzle_input]
    for row_index, row in enumerate(puzzle_matrix):
        for c_index, c in enumerate(row):
            if c in numbers:
                number_indexes[(row_index, c_index)] = c
            if c not in numbers and c != '.':
                symbol_indexes.append((row_index, c_index))
            if c == '*':
                gear_indexes[(row_index, c_index)] = []

    for coordinates, value in number_indexes.items():
        x, y = coordinates
        num = value
        end_y = y
        is_first = (x, y-1) not in number_indexes
        if is_first:
            i = 1
            while (x, y+i) in number_indexes:
                num += number_indexes[x, y+i]
                end_y = y+i
                i += 1
            found_numbers.append(dict(
                value=int(num),
                row=x,
                position_start=y,
                position_end=end_y,
            ))

    result = 0
    result2 = 0

    for number in found_numbers:
        symbol_rows = (number['row']-1, number['row'], number['row']+1)
        symbol_pos = range(number['position_start']-1, number['position_end']+2)
        possible_adjecent_indices = product(symbol_rows, symbol_pos)
        for i in possible_adjecent_indices:
            symbol_found = False
            if i in symbol_indexes:
                symbol_found = True
            if i in gear_indexes:
                gear_indexes[i].append(number)
            if symbol_found:
                result += number['value']

    for gear, n in gear_indexes.items():
        if len(n) == 2:
            result2 += n[0]['value'] * n[1]['value']

    print(result)
    print(result2)


if __name__ == '__main__':
    main()
