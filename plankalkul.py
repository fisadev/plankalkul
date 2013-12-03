# coding: utf-8
from collections import Counter
from itertools import combinations
from operator import itemgetter


GAMES = (
    'straight-flush',  # Cinco cartas consecutivas del mismo palo.
    'four-of-a-kind',  # Cuatro cartas iguales en su valor
    'full-house',  # Tres cartas iguales en su valor (trío), más otras dos iguales en su valor (pareja).
    'flush',  # Cinco cartas del mismo color y palo, sin ser necesariamente consecutivas.
    'straight',  # Cinco cartas consecutivas sin importar el palo.
    'three-of-a-kind',  # Tres cartas iguales de valor.
    'two-pairs',  # Dos pares de cartas del mismo número (par y par).
    'one-pair',  # Dos cartas iguales de número (y tres diferentes).
    'highest-card',  # Gana quien tiene la carta más alta de todas.
)


def guess(hand, deck):
    hand, deck = [tuple(x.split())
                  for x in (hand, deck)]

    for game in GAMES:
        if check(game, hand, deck):
            return game


def check(game, hand, deck):
    checker = globals().get('check_' + game.replace('-', '_'))

    if not checker:
        raise NotImplemented('Unkown game: ' + game)

    for take_count in range(len(deck) + 1):
        take = deck[:take_count]

        possible_keeps = combinations(hand, len(hand) - take_count)
        new_hands = [keep + take for keep in possible_keeps]

        if any(map(checker, new_hands)):
            return True

    return False


def get_numbers(cards):
    def to_int(number_part):
        letters = {'a': 1, 't': 10, 'j': 11, 'q': 12, 'k': 13}
        if number_part in letters:
            return letters[number_part]
        else:
            return int(number_part)

    return [to_int(card[0]) for card in cards]


def get_suits(cards):
    return map(itemgetter(1), cards)


def count_numbers(cards):
    return Counter(get_numbers(cards))

def repeated_numbers(cards, min_repetitions=2):
    counts = count_numbers(cards)
    return [number for number, count in counts.items()
            if count >= min_repetitions]


def check_straight_flush(cards):
    return check_flush(cards) and check_straight(cards)


def check_four_of_a_kind(cards):
    return len(repeated_numbers(cards, 4)) > 0


def check_full_house(cards):
    counts = count_numbers(cards)
    return set(counts.values()) == set((2, 3))


def check_flush(cards):
    return len(set(get_suits(cards))) == 1


def check_straight(cards):
    numbers = list(sorted(get_numbers(cards)))
    first = numbers[0]
    expected_numbers = range(first, first + len(numbers))

    return numbers == expected_numbers


def check_three_of_a_kind(cards):
    return len(repeated_numbers(cards, 3)) > 0


def check_two_pairs(cards):
    return len(repeated_numbers(cards)) > 1


def check_one_pair(cards):
    return len(repeated_numbers(cards)) > 0


def check_highest_card(cards):
    return True
