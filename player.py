
class player:
    def __init__(self):
        self.handOfCards = []
    
    def drowCard(self,card):
        self.handOfCards += [card]
    
    def showHandOfCards(self):
        # ♠♡♢♣♤♥♦♧
        cardTypeDict = {"spade":"♤","heart":"♥","diamond":"♢","club":"♣"}
        for card in self.handOfCards:
            print(cardTypeDict[card.type]+str(card.number),end=' ')