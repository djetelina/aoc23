from math import prod
from pathlib import Path

STARTING_SPEED = 0
ACCELERATION = 1


def main():
    with open(Path.cwd() / 'inputs' / '6.txt', 'r') as f:
        puzzle_input = f.readlines()

#     puzzle_input = """Time:      7  15   30
# Distance:  9  40  200"""

    times, distances = puzzle_input
    times = int(times.split(':')[1].replace(' ', ''))
    distances = int(distances.split(':')[1].replace(' ', ''))
    races = [(times, distances)]

    possible_record_breakings = []

    for race in races:
        race_records = 0
        for i in range(race[0]):
            button_held = i
            traveled = i * ACCELERATION * (race[0] - button_held)
            if traveled > race[1]:
                race_records += 1
        possible_record_breakings.append(race_records)

    result = prod(possible_record_breakings)
    print(result)


if __name__ == '__main__':
    main()
