from Field import Field
import BasicStrategy_basic

class blackJack(Field):
    # blackJack
    def playerMode(self):
        print("\nplayerCardDeck")
        self.player.showHandOfCards()
        burstRate = self.burstRate()
        print("\nバースト率: "+str(burstRate)+"%")
        recommendedAction = self.recommendedAction()
        print("\n推奨アクション: ",recommendedAction)
        while True:
            val = input('\naction: ')
            if val == "hit" or val == "Hit":
                self.player.drowCard(self.playingCard.drowCard()) 
                sumNum = self.getSumNum(self.player.handOfCards)
                print("playerCardDeck")
                self.player.showHandOfCards()
                burstRate = self.burstRate()
                print("\nバースト率: "+str(burstRate)+"%")
                recommendedAction = self.recommendedAction()
                print("\n推奨アクション: ",recommendedAction)
            elif val == "stand" or val == "Stand":
                break
            elif val == "double up" or "double":
                self.player.addchip(self.betedChip)
                isChip = self.player.betChip(self.betedChip*2)
                if not isChip:
                    print("ダブルアップできません")
                    pass
                self.betedChip *= 2
                self.player.drowCard(self.playingCard.drowCard())
                # sumNum = self.getSumNum(self.player.handOfCards)
                print("playerCardDeck")
                self.player.showHandOfCards() 
                break
            else:
                pass
            if sumNum > 21:
                break

    # バースト率の計算場所...
    # よりかっこよく計算できるようにしたい
    def burstRate(self):
        sumNum = self.getSumNum(self.player.handOfCards)
        upperLimit = 21 -sumNum
        burstRate = 0
        cardNums = [0,4,4,4,4,4,4,4,4,4,16]
        if self.gameMaster.handOfCards[0].number >= 10:
            cardNums[10] -= 1
        else:
            cardNums[self.gameMaster.handOfCards[0].number] -= 1
        for card in self.player.handOfCards:
            if card.number >= 10:
                cardNums[10] -= 1
            else:
                cardNums[card.number] -= 1
        for cpu in self.cpu:
            for card in cpu.handOfCards:
                if card.number >= 10:
                    cardNums[10] -= 1
                else:
                    cardNums[card.number] -= 1
        remainingCards = sum(cardNums)
        if upperLimit < 0:
            burstRate = 1
        elif upperLimit >= 0 and upperLimit < 10:
            for i in range(upperLimit,len(cardNums)):
                burstRate += cardNums[i]
            burstRate /= remainingCards
        return burstRate*100

    def recommendedAction(self):
        action = ""
        gameMasterCardNum = self.gameMaster.handOfCards[0].number
        if gameMasterCardNum > 10:
            gameMasterCardNum = 10
        if self.getSumNum(self.player.handOfCards) <= 8:
            action = BasicStrategy_basic.list[0][gameMasterCardNum-1]
        elif self.getSumNum(self.player.handOfCards) >= 17:
            action = BasicStrategy_basic.list[9][gameMasterCardNum-1]
        else:
            action = BasicStrategy_basic.list[self.getSumNum(self.player.handOfCards)%9+1][gameMasterCardNum-1]
        return action

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

    def getSumNum(self,cardDeck):
        tmpCardDeck = []
        for card in cardDeck:
            tmpCardDeck += [card.number]
        tmpCardDeck.sort(reverse=True)
        sumNum = 0
        for num in tmpCardDeck:
                if num > 10:
                    sumNum += 10
                elif num == 1 and sumNum + 11 > 21:
                    sumNum += num
                elif num == 1 and sumNum + 11 <= 21:
                    sumNum += num + 10
                else:
                    sumNum += num
        return sumNum

    def duel(self):
        status = ""
        playerSumNum = self.getSumNum(self.player.handOfCards)
        gameMasterSumNum = self.getSumNum(self.gameMaster.handOfCards)
        if playerSumNum >= 22 and gameMasterSumNum >= 22:
            print("player Lose")
            status = "Lose"
        elif playerSumNum < 22 and gameMasterSumNum >= 22:
            print("player Win")
            status = "Win"
        elif playerSumNum >= 22 and gameMasterSumNum < 22:
            print("player Lose")
            status = "Lose"
        elif playerSumNum > gameMasterSumNum:
            print("player Win")
            status = "Win"
        elif playerSumNum < gameMasterSumNum:
            print("player Lose")
            status = "Lose"
        else:
            print("Drow")
            status = "Drow"
        return status

    def returnChip(self,status):
        if status == "Win":
            print(str(self.betedChip*2)+"枚ゲット")
            self.player.addchip(self.betedChip*2)
        elif status == "Drow":
            print(str(self.betedChip)+"枚ゲット")
            self.player.addchip(self.betedChip)
        else:
            pass   
        print("現在"+str(self.player.chip)+"枚")

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