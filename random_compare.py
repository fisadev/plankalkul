# coding: utf-8
import sys
from random import sample


NUMBERS = '23456789tjqka'
SUITS = 'cdhs'
ALL_CARDS = [n + s for n in NUMBERS for s in SUITS]


guessers = [__import__(module).guess
            for module in sys.argv[1:]]


while True:
    cards = sample(ALL_CARDS, 10)
    hand, deck = map(' '.join, (cards[:5], cards[5:]))

    results = [guesser(hand, deck) for guesser in guessers]

    print hand, '-', deck, '|',
    if len(set(results)) != 1:
        results_text = ['%s:%s' % (guesser.__module__, result)
                        for guesser, result in zip(guessers, results)]
        print 'DIFF', ' '.join(results_text)
    else:
        print 'OK'
