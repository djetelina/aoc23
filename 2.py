import re
from pathlib import Path

games = {}
available = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def main():
    with open(Path.cwd() / 'inputs' / '2.txt', 'r') as f:
        puzzle_input = f.readlines()

    for game in puzzle_input:
        game_number = re.findall(r'Game (\d+)', game)[0]
        sets = game.split(':')[1].split(';')
        game_info = {}
        power_of_balls = 1
        for color in available:
            max_played = 0
            for game_set in sets:
                played = re.findall(f'(\d+) {color}', game_set)
                if played and int(played[0]) > max_played:
                    max_played = int(played[0])
            game_info[color] = max_played
            power_of_balls *= max_played
        game_info['possible'] = all([max <= available[color] for color, max in game_info.items()])
        game_info['pow'] = power_of_balls
        games[int(game_number)] = game_info

    print(sum(game for game, info in games.items() if info['possible']))
    print(sum(info['pow'] for info in games.values()))


if __name__ == '__main__':
    main()
