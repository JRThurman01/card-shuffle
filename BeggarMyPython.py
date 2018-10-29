#!/usr/bin/env python3

from random import sample



def penalty_value_of(card):
    values = {"J": 1, "Q": 2, "K": 3, "A": 4}
    return values[card]


def play(hands, firstCardOnLeft=True, verbose=False, maxTricks = 1000):
    a, b = hands  # hands are called a and b
#    print("Starting hands: %s/%s" % (a, b))
    if not firstCardOnLeft:
        a.reverse()
        b.reverse()
    stack = ""  # cards in the middle
    turns = 0
    tricks = 0
    player = 1  # alternates between 1 and -1
    while a != "" and b != "":  # game terminates when a or b's hands are empty
        battle_in_progress = False
        cards_to_play = 1
        while cards_to_play > 0:  # current player may play up to cards_to_play cards

            try:
                if player == 1:
                    # grab next card from first character of string a
                    next_card = a[0]
                    a = a[1:]
                else:
                    # grab next card from first character of string b
                    next_card = b[0]
                    b = b[1:]
            except IndexError:
                break  # ran out of cards to play, game over...

            turns = turns + 1

            stack = stack + next_card  # add to the stack

            if next_card == '-':
                # not a court card
                if battle_in_progress:
                    cards_to_play = cards_to_play - 1  # this player needs keep trying to find a court card
                else:
                    player = player * -1  # no court cards found yet, back to other player
            else:
                # court card found, back to the other player
                battle_in_progress = True
                cards_to_play = penalty_value_of(next_card)
                player = player * -1

        # end of trick, make the losing player pick up the cards in the stack
        tricks = tricks + 1
        if player == 1:
            b = b + stack
            stack = ''
        else:
            a = a + stack
            stack = ''

        player = player * -1

        # print current status
        if verbose:
            print("%s/%s/%s" % (a, b, stack))

        if tricks >= maxTricks:
            file = open('unfinished_games.csv', 'a')
            file.write('Hand1: {} \n'.format(hands[0]))
            file.write('Hand2: {} \n'.format(hands[1]))
            file.write('Tricks: {} \n'.format(tricks))
            file.write('Turns: {} \n \n'.format(turns))
            file.close()
            a="" #Force finish

    return((turns, tricks))

    #print("There were %d turns" % turns)
    #print("There were %d tricks\n" % tricks)

class ShuffledDeck(object):
    #Define the deck:
    deck_cards = [(36, '-'), (4, 'J'), (4, 'Q'), (4, 'K'), (4, 'A')] #[(36, '-'), (4, 'J'), (4, 'Q'), (4, 'K'), (4, 'A')]


    def __init__(self):
        self.card_permutation =[]
        self.cards= []
        for number, card in self.deck_cards:
            self.card_permutation.extend([number*[0]])
            #self.card_permutation = [36*[0], 4*[0], 4*[0],4*[0], 4*[0]]
            self.cards.insert(0, card)
            #['A', 'K', 'Q', 'J', '-']

    def deck(self):
        deck=""
        for counter in range(0, len(self.deck_cards)):
            (number_of_cards, card) = self.deck_cards[counter]
            permutation = self.card_permutation[counter]
            for i in range(0,number_of_cards):
                deck = deck[:permutation[i]] + card + deck[permutation[i]:]
        return deck

    def next_deck(self):
        self.card_permutation =self.iterate(0, self.deck_cards[:], self.card_permutation[:])


    def iterate(self, deck_size, deck_cards, card_permutation):

        (number_of_cards, card) = deck_cards.pop(0)
        permutation = card_permutation.pop(0)

        if permutation == number_of_cards * [deck_size]:
            permutation = number_of_cards * [0]
            card_permutation = self.iterate(deck_size+number_of_cards, deck_cards, card_permutation[:])
        else:
            # Find the first non-maximal value and at one. All
            current_number = [x for x in permutation if x not in [deck_size]][0]  #The first item not equal to deck size
            index_number = permutation.index(current_number)
            for j in range(0, index_number+1):
                permutation[j] = current_number+1

        card_permutation.insert(0, permutation)
        return card_permutation

    def set_seed(self, seed):

        if isinstance(seed, str):
            seed = list(seed)

        card_permutation = []

        temp_dict = seed[:]
        for card in self.cards:

            permutation = [i for i, val in enumerate(temp_dict) if val == card]
            permutation.reverse()

            length = len(permutation)
            for i in range(0, length):
                permutation[i]= permutation[i] - length+i+1

            temp_dict= a = [x for x in temp_dict if x != card]
            card_permutation.insert(0, permutation)

        self.card_permutation = card_permutation

    def dict_to_string(self, dictionary):
        return ''.join(dictionary)

    def deal(self):
        deck = self.deck()
        return (deck[::2], deck[1::2])

    def random(self):
        temp_deck = self.deck()
        temp_deck = ''.join(sample(temp_deck,len(temp_deck)))
        self.set_seed(temp_deck)


if __name__ == '__main__':
    shuffled_deck = ShuffledDeck()
    shuffled_deck.random()
    try:
        file_counter = 0
        while True:  # for i in range(0,10000):
            with open('run1/result{}.csv' .format(file_counter), 'w') as file:
                file.write('starting_deck = {} \n'.format(shuffled_deck.deck()))
                file.write('starting_deck_config = {} \n' .format(shuffled_deck.card_permutation))
                file.write('Run Number,Hands,Tricks\n')

                run_counter = 0
                for i in range(0,1000000): # limiting to 1m to make reading this easier

                        hand = shuffled_deck.deal()
                        result = play(hand, verbose=False, maxTricks=1000) #Normally 1000
                        file.write('{},{},{} \n' .format(run_counter, result[0], result[1]))
                        shuffled_deck.next_deck()
                        run_counter +=1
            file.close()
            file_counter += 1
    finally:
        file.close()
