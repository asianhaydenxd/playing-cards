import random

class Card:
    # initializes the suit and number of the card
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
    
    # use Deck.cards[x].name() to get the card name
    def name(self):
        val = str(self.num)

        # renames the number in special cases
        if val == '11':
            val = 'Jack'
        elif val == '12':
            val = 'Queen'
        elif val == '13':
            val = 'King'
        elif val == '1':
            val = 'Ace'
        
        return(f'{val} of {self.suit}')

class Deck:
    # construct a new Deck object
    def __init__(self):
        self.cards = []

        # creates a new item in cards for each of the 52 cards in a standard deck
        for num in range(1,14):
            for suit in ['Hearts', 'Spades', 'Clubs', 'Diamonds']:
                self.cards.append(Card(suit, num))
    
    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)
    
    def printcards(self):
        temp = []
        for i in self.cards:
            temp.append(i.name())
        print(temp)
