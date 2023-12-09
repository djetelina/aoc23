from pathlib import Path


def extrapolate(sequence):
    if all([i == 0 for i in sequence]):
        return 0
    lower_sequence = []
    for a, b in enumerate(sequence):
        if a == 0:
            continue
        else:
            lower_sequence.append(b - sequence[a-1])
    next_lower = extrapolate(lower_sequence)
    return sequence[-1] + next_lower


def extrapolate_back(sequence):
    if all([i == 0 for i in sequence]):
        return 0
    lower_sequence = []
    for a, b in enumerate(sequence):
        if a == len(sequence) - 1:
            continue
        else:
            lower_sequence.insert(0, sequence[a+1] - b)
    next_lower = extrapolate(lower_sequence)
    return sequence[0] - next_lower

def main():
    with open(Path.cwd() / 'inputs' / '9.txt', 'r') as f:
        puzzle_input = f.readlines()

#     puzzle_input = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45""".split('\n')

    sum = 0
    sum_back = 0
    for line in puzzle_input:
        l = [int(x) for x in line.split()]
        sum += extrapolate(l)
        sum_back += extrapolate_back(l)

    print(sum)
    print(sum_back)




if __name__ == '__main__':
    main()
