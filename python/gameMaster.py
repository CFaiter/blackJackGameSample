
class gameMaster:
    def __init__(self):
        self.handOfCards = []
    
    def resetHandOfCards(self):
        self.handOfCards = []

    def drowCard(self,card):
        self.handOfCards += [card]
    
    def showOnlyOneHandOfCards(self):
        # ♠♡♢♣♤♥♦♧
        cardTypeDict = {"spade":"♤","heart":"♥","diamond":"♢","club":"♣"}
        print(cardTypeDict[self.handOfCards[0].type]+str(self.handOfCards[0].number),end=' ')
    
    def showAllHandOfCards(self):
        # ♠♡♢♣♤♥♦♧
        cardTypeDict = {"spade":"♤","heart":"♥","diamond":"♢","club":"♣"}
        for card in self.handOfCards:
            print(cardTypeDict[card.type]+str(card.number),end=' ')