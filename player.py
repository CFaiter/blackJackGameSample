
class player:
    def __init__(self):
        self.handOfCards = []
        self.chip = 0
    
    def resetHandOfCards(self):
        self.handOfCards = []

    def drowCard(self,card):
        self.handOfCards += [card]
    
    def addchip(self,money):
        self.chip += money

    def betChip(self,chip):
        if self.chip-chip >= 0:
            print(str(chip)+"枚ベット")
            self.chip -= chip
            return True
        else:
            print("チップが足りません！")
            return False

    def showHandOfCards(self):
        # ♠♡♢♣♤♥♦♧
        cardTypeDict = {"spade":"♤","heart":"♥","diamond":"♢","club":"♣"}
        for card in self.handOfCards:
            print(cardTypeDict[card.type]+str(card.number),end=' ')
        
    def showChip(self):
        print("チップ数: "+str(self.chip))