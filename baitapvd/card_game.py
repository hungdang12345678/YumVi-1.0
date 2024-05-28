import random
class Card:
    rank_names =[None, "Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    suit_names = ["Hearts","Diamonds","Clubs","Spades"]
    def _init_(self, rank=3, suit=3):
        self.rank = rank
        self.suit = suit
    
    def _str_(self):
        return "%s of %s" % (self.rank_names[self.rank], self.suit_names[self.suit])

class Deck:
    def _init_(self):
        self.cards =[]
        for i in range (1,14):
            for j in range (4):
                card = Card(i,j)
                self.cards.append(card)

    def _str_(self):
        res =[]
        for item in self.cards:
            res.append(str(item))
        return "\n".join(res)
    
    def shuffle(self):
        random.shuffle(self.cards)
        return self
    
    def draw(self):
        return self.cards.pop(0)
    
class Hand:

    def _init_(self,deck):
        self.cards = []
        for item in range (3):
            card = deck.draw()
            self.cards.append(card)

deck = Deck()
deck_new = deck.shuffle()
hand = Hand(deck_new)
for item in hand.cards:
    print(item)

