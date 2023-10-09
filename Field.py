from cardList import cardList
from player import player
from gameMaster import gameMaster

class Field:
    def __init__(self):
        self.betedChip = 0
        self.playingCard = cardList()
        self.gameMaster = gameMaster()
        self.player = player()
        self.cpu = []
    
    def unit(self,cpuNum):
        self.betedChip = 0
        self.playingCard.unit()
        self.playingCard.shuffleCardDeck()
        self.gameMaster.resetHandOfCards()
        self.player.resetHandOfCards()
        for i in range(2):
            self.gameMaster.drowCard(self.playingCard.drowCard())
        for i in range(2):
            self.player.drowCard(self.playingCard.drowCard())
        # self.player.addchip(1000)
        self.cpu = []
        for i in range(cpuNum):
            cpu = player()
            cpu.resetHandOfCards()
            for j in range(2):
                cpu.drowCard(self.playingCard.drowCard())
            self.cpu += [cpu]

    def changeChip(self,money):
        self.player.addchip(money)

    def callBetChip(self):
        val = input('\n:How many chips do you want to bet?: ')
        playerBetChip = int(val)
        isChip = self.player.betChip(playerBetChip)
        if isChip:
            self.betedChip = playerBetChip
        else:
            self.betedChip = 0
    