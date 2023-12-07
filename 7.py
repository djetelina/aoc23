from collections import Counter
from pathlib import Path


# part 1 cards
# CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDS = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
TYPE_SORTING_SCORE = {
    'five_of_a_kind': 10**16,
    'four_of_a_kind': 10**15,
    'full_house': 10**14,
    'three_of_a_kind': 10**13,
    'two_pair': 10**12,
    'one_pair': 10**11,
    'high_card': 10**10
}


def sort_hand(hand):
    hand, _ = hand
    counted_hand = Counter(hand).most_common()
    # PART 2 start
    if 'J' in hand:
        i = 0 if 'J' != counted_hand[0][0] or len(counted_hand) == 1 else 1
        copied_hand = hand.replace('J', counted_hand[i][0])
    else:
        copied_hand = hand
    counted_hand = Counter(copied_hand).most_common()
    # PART 2 end

    if len(counted_hand) == 1:
        sorting_score = TYPE_SORTING_SCORE['five_of_a_kind']
    elif counted_hand[0][1] == 4:
        sorting_score = TYPE_SORTING_SCORE['four_of_a_kind']
    elif counted_hand[0][1] == 3 and counted_hand[1][1] == 2:
        sorting_score = TYPE_SORTING_SCORE['full_house']
    elif counted_hand[0][1] == 3:
        sorting_score = TYPE_SORTING_SCORE['three_of_a_kind']
    elif counted_hand[0][1] == 2 and counted_hand[1][1] == 2:
        sorting_score = TYPE_SORTING_SCORE['two_pair']
    elif counted_hand[0][1] == 2:
        sorting_score = TYPE_SORTING_SCORE['one_pair']
    else:
        sorting_score = TYPE_SORTING_SCORE['high_card']

    return sorting_score, CARDS.index(hand[0][0]), CARDS.index(hand[1][0]), CARDS.index(hand[2][0]), CARDS.index(hand[3][0]), CARDS.index(hand[4][0])


def main():
    with open(Path.cwd() / 'inputs' / '7.txt', 'r') as f:
        puzzle_input = f.readlines()

#     puzzle_input = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483""".split('\n')

    hands = []
    for l in puzzle_input:
        hand, bid = l.split(" ")
        hands.append((hand, int(bid.strip())))

    sorted_hands = sorted(hands, key=sort_hand)

    total = 0
    rank = 1
    for hand in sorted_hands:
        total += hand[1] * rank
        rank += 1

    print(total)


if __name__ == '__main__':
    main()
