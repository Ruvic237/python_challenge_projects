import random
# Deck of cards: Q,K,J is 10 and Ace is 1 or 11
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

class Cards:
    
    def __init__(self):
        self.score = 0
        self.card = []
        
        
    # method to pick cards
    def pick(self):
        for i in range (2):
            x = random.choice(cards)
            self.card.append(x)
        self.score = sum(self.card)
        