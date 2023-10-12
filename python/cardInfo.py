class cardInfo:
    def __init__(self):
        self.type = ""
        self.number = 0
    
    def addType(self,type):
        self.type = type

    def addNumber(self,num):
        self.number = num

    def showCard(self):
        cardTypeDict = {"spade":"♤","heart":"♥","diamond":"♢","club":"♣"}
        print(cardTypeDict[self.type]+str(self.number))