from collections import defaultdict
from itertools import product
from math import lcm
from pathlib import Path


def loop_over_directions(directions):
    while True:
        for d in directions:
            yield d


def main():
    with open(Path.cwd() / 'inputs' / '8.txt', 'r') as f:
        puzzle_input = f.readlines()

#     puzzle_input = """LLR
#
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)""".split('\n')

#     puzzle_input = """LR
#
# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)""".split('\n')

    directions, _, *raw_nodes = puzzle_input
    directions = directions.strip()

    nodes = {}
    for node in raw_nodes:
        name = node.split('=')[0].strip()
        left = node.split('(')[1].split(',')[0].strip()
        right = node.split(',')[1].split(')')[0].strip()
        nodes[name] = dict(L=left, R=right)

    # current = 'AAA'
    # destination = 'ZZZ'
    # steps = 0
    # for direction in loop_over_directions(directions):
    #     if current == destination:
    #         break
    #     current = nodes[current][direction]
    #     steps += 1
    #
    # print(f'PT1 Total steps: {steps}')

    currents = [k for k in nodes.keys() if k.endswith('A')]
    found = False
    mults = defaultdict(list)

    pt2_steps = 0
    for direction in loop_over_directions(directions):
        should_break = []
        for i, c in enumerate(currents):
            if c.endswith('Z'):
                should_break.append(True)
                mults[i].append(pt2_steps)
            else:
                should_break.append(False)
            currents[i] = nodes[c][direction]
        if all(should_break):
            found = True
            break
        if len(mults.values()) == len(currents) and all(len(m) >= 5 for m in mults.values()):
            break
        pt2_steps += 1
    if found:
        print(f'PT2 Total steps: {pt2_steps}')
    lcms = []
    if not found:
        for p in product(*mults.values()):
            lcms.append(lcm(*p))
    print(f'PT2 Total steps: {min(lcms)}')


if __name__ == '__main__':
    main()
