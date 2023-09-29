from cardList import cardList
from player import player
from gameMaster import gameMaster

class Field:
    def __init__(self):
        self.playingCard = cardList()
        self.gameMaster = gameMaster()
        self.player = player()
        self.cpu = []
    
    def unit(self):
        self.playingCard.unit()
        self.playingCard.shuffleCardDeck()
        for i in range(2):
            self.gameMaster.drowCard(self.playingCard.drowCard())
        for i in range(2):
            self.player.drowCard(self.playingCard.drowCard())
        cpuNum = 3
        for i in range(cpuNum):
            cpu = player()
            for j in range(2):
                cpu.drowCard(self.playingCard.drowCard())
            self.cpu += [cpu]

    
    def playerMode(self):
        print("\nplayerCardDeck")
        self.player.showHandOfCards()
        while True:
            val = input('\naction: ')
            if val == "hit" or val == "Hit":
                self.player.drowCard(self.playingCard.drowCard()) 
                sumNum = self.getSumNum(self.player.handOfCards)
                print("playerCardDeck")
                self.player.showHandOfCards()
            elif val == "stand" or val == "Stand":
                break
            else:
                pass

            if sumNum > 21:
                # print("\nBurst!!!")
                break
            

    def gameMasterMode(self):
        # self.gameMaster.showHandOfCards()
        while True:
            sumNum = self.getSumNum(self.gameMaster.handOfCards)
            if sumNum >= 17:
                break
            else:
                self.gameMaster.drowCard(self.playingCard.drowCard()) 
                # self.gameMaster.showHandOfCards()
        print()
        print("gameMasterCardDeck")
        self.gameMaster.showAllHandOfCards()
    
    def cpuMode(self):
        i = 1
        for cpu in self.cpu:
            while True:
                sumNum = self.getSumNum(cpu.handOfCards)
                if sumNum >= 17:
                    break
                else:
                    cpu.drowCard(self.playingCard.drowCard()) 
                    # self.gameMaster.showHandOfCards()
            print()
            print("cpu"+str(i))
            cpu.showHandOfCards()
            i+=1

    def duel(self):
        playerSumNum = self.getSumNum(self.player.handOfCards)
        gameMasterSumNum = self.getSumNum(self.gameMaster.handOfCards)
        if playerSumNum < 22 and gameMasterSumNum >= 22:
            print("player Win")
        elif playerSumNum >= 22 and gameMasterSumNum < 22:
            print("player Lose")
        elif playerSumNum > gameMasterSumNum:
            print("player Win")
        elif playerSumNum < gameMasterSumNum:
            print("player Lose")
        else:
            print("Drow")

    def getSumNum(self,cardDeck):
        cardDeck.sort(key=lambda x: x.number, reverse=True)
        sumNum = 0
        for card in cardDeck:
                num = card.number
                if num > 10:
                    sumNum += 10
                elif num == 1 and sumNum + 11 > 21:
                    sumNum += num
                elif num == 1 and sumNum + 11 <= 21:
                    sumNum += num + 10
                else:
                    sumNum += num
        return sumNum

    def showField(self):
        print("gameMasterCardDeck")
        self.gameMaster.showOnlyOneHandOfCards()
        i = 1
        for cpu in self.cpu:
            print("\ncpu"+str(i)+"CardDeck")
            cpu.showHandOfCards()
            i += 1
        print("\nplayerCardDeck")
        self.player.showHandOfCards()