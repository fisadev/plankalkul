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
    return map(itemgetter(0), cards)


def get_suits(cards):
    return map(itemgetter(1), cards)


def check_two_pairs(cards):
    numbers = get_numbers(cards)
    counts = Counter(numbers)

    repeated = [number for number, count in counts.items()
                if count > 1]

    return len(repeated) > 1


def check_one_pair(cards):
    numbers = get_numbers(cards)
    return len(set(numbers)) < len(cards)


def check_highest_card(cards):
    return True
