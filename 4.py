from pathlib import Path


def main():
    with open(Path.cwd() / 'inputs' / '4.txt', 'r') as f:
        puzzle_input = f.readlines()

    score = 0
    cards = []

    for card in puzzle_input:
        winning_numbers, my_numbers = card.split(':')[1].split('|')
        winning_numbers = [n.strip() for n in winning_numbers.split(' ') if n]
        my_numbers = [n.strip() for n in my_numbers.split(' ') if n]
        numbers_won = [n for n in my_numbers if n in winning_numbers]
        cards.append({'numbers_won': len(numbers_won), 'copies': 1})
        card_score = 0
        if numbers_won:
            card_score = 1
            for i in range(len(numbers_won) - 1):
                card_score *= 2
        score += card_score

    print(score)

    for i, card in enumerate(cards):
        for _ in range(card['numbers_won']):
            i += 1
            try:
                cards[i]['copies'] += card['copies']
            except IndexError:
                break

    print(sum(c['copies'] for c in cards))


if __name__ == '__main__':
    main()
