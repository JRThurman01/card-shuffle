from BeggarMyPython import play, penalty_value_of, ShuffledDeck
import pandas as pd
from matplotlib import pyplot as plt

def test_createhands():
    shuffled_deck = ShuffledDeck()
    print(shuffled_deck.deck())
    print(shuffled_deck.deal())

def test_test_hand():
    shuffled_deck = ShuffledDeck()
    print(shuffled_deck.deck())
    hand = shuffled_deck.deal()
    play(hand, verbose=False)

def test_lotsofhands():
    shuffled_deck = ShuffledDeck()

    for i in range(0,100):
        hand = shuffled_deck.deal()
        play(hand, verbose=False)
        shuffled_deck.next_deck()



def test_randomhands():
    shuffled_deck = ShuffledDeck()
    shuffled_deck.random()

    for i in range(0,100):
        hand = shuffled_deck.deal()
        play(hand, verbose=False)
        shuffled_deck.next_deck()
