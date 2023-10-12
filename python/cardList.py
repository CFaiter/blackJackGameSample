from cardInfo import cardInfo

import random

class cardList:
    def __init__(self):
        self.cardDeck = []
    
    def addCardDeck(self,card):
        self.cardDeck += [card]

    def unit(self):
        typeList = ["spade","heart","diamond","club"]
        for typeName in typeList:
            for i in range(13):
                card = cardInfo()
                card.addType(typeName)
                card.addNumber(i+1)
                self.addCardDeck(card)
    
    def shuffleCardDeck(self):
        random.shuffle(self.cardDeck)

    def drowCard(self):
        drowedCard = self.cardDeck.pop()
        return drowedCard
    
    def showCardDeck(self):
        for card in self.cardDeck:
            card.showCard()
