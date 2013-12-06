# coding: utf-8
from random import sample

from plankalkul import guess as plankalkul_guess
from wanks import guess as wanks_guess
from face import guess as face_guess


guessers = [plankalkul_guess, wanks_guess, face_guess]


NUMBERS = '23456789tjqka'
SUITS = 'cdhs'
ALL_CARDS = [n + s for n in NUMBERS for s in SUITS]


while True:
    cards = sample(ALL_CARDS, 10)
    hand, deck = map(' '.join, (cards[:5], cards[5:]))

    results = [guesser(hand, deck) for guesser in guessers]

    print hand, '-', deck,
    if len(set(results)) != 1:
        print 'Difference!',
        for guesser, result in zip(guessers, results):
            print guesser.__module__, result,
    else:
        print 'Ok',

    print ''
