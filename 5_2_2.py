import re
from pathlib import Path


def input_map_to_ranges(i):
    all_lines = [l for l in i.split(':')[1].split('\n') if l]
    ranges = []
    for l in all_lines:
        dest_range_start, source_range_start, length = [int(n) for n in l.split(' ')]
        ranges.append(dict(
            dest=range(dest_range_start, dest_range_start+length),
            source=range(source_range_start, source_range_start+length)
        ))
    return ranges


def main():
    with open(Path.cwd() / 'inputs' / '5.txt', 'r') as f:
        puzzle_input = f.read()

    seeds, *maps = puzzle_input.split('\n\n')
    maps = [input_map_to_ranges(m) for m in maps]
    maps.reverse()
    seed_pairs = re.findall(r'(\d+ \d+)', seeds)
    seed_pairs_ranges = []
    for sp in seed_pairs:
        start, length = sp.split(' ')
        seed_pairs_ranges.append(range(int(start), int(start)+int(length)))

    location = 0
    while True:
        if location % 1_000_000 == 0:
            print(location)
        i = location
        for ranges in maps:
            for r in ranges:
                try:
                    ind = r['dest'].index(i)
                    i = r['source'][ind]
                    break
                except ValueError:
                    continue
        for s_r in seed_pairs_ranges:
            if i in s_r:
                print(location)
                exit(0)
        location += 1


if __name__ == '__main__':
    main()
