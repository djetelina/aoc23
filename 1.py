import re
from pathlib import Path


spelled_numbers = {
    'one': 'one1one',
    'two': 'two2two',
    'three': 'three3three',
    'four': 'four4four',
    'five': 'five5five',
    'six': 'six6six',
    'seven': 'seven7seven',
    'eight': 'eight8eight',
    'nine': 'nine9nine'
}


def main(part=1):
    with open(Path.cwd() / 'inputs' / '1.txt', 'r') as f:
        puzzle_input = f.readlines()

    result = 0

    for line in puzzle_input:
        line = line.strip()
        if part == 2:
            for w, n in spelled_numbers.items():
                line = line.replace(w, n)
        all_numbers = ''.join(re.findall(r'\d+', line))
        result += int(f'{all_numbers[0]}{all_numbers[-1]}')
    print(result)


if __name__ == '__main__':
    main()
    main(2)
