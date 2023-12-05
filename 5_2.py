import re
from multiprocessing import Pool
from pathlib import Path


def iterate_over_seeds(seed_pairs):
    for pair in seed_pairs:
        start, length = pair.split(' ')
        yield from range(int(start), int(start)+int(length))


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


def deep_dive(seeds, maps, length='2037733040', worker=0):
    lowest = 10000000000000000000000000
    c = 0
    for seed in seeds:
        if c % 100_000 == 0:
            print(f'W{worker}: {int(c/int(length)*10000)/100}% seeds processed ({c}/{length})')
        c += 1
        current_lookup = seed
        for m in maps:
            for line in m:
                try:
                    i = line['source'].index(current_lookup)
                    current_lookup = line['dest'][i]
                    break
                except ValueError:
                    continue
        if current_lookup < lowest:
            lowest = current_lookup
            print(f'New lowest location for W{worker}: {lowest} from seed {seed}')
    return lowest


def main():
    with open(Path.cwd() / 'inputs' / '5.txt', 'r') as f:
        puzzle_input = f.read()

    seeds, *maps = puzzle_input.split('\n\n')
    maps = [input_map_to_ranges(m) for m in maps]
    seed_pairs = re.findall(r'(\d+ \d+)', seeds)
    ranges = []
    for pair in seed_pairs:
        start, length = pair.split(' ')
        ranges.append((range(int(start), int(start)+int(length)), length))
    with Pool(len(ranges)) as p:
        args = [(r[0], maps, r[1], i) for i, r in enumerate(ranges)]
        lowest = p.starmap(deep_dive, args)

    print(f'Final lowest location: {min(lowest)}')


if __name__ == '__main__':
    main()

41625660
