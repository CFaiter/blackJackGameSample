from Field import Field

class baccarat(Field):
    # カードの値を計算する関数
    def calculate_hand_value(self,hand):
        sum = 0
        for card in hand:
            if card.number < 10:
                sum += card.number
        return sum%10
    
    def judgeDrow(self):
        isDrow = True
        # プレイヤーが3枚目のカードを引くかどうかを決定 
        if self.calculate_hand_value(self.player.handOfCards) <= 5: 
            self.player.drowCard(self.playingCard.drowCard()) 
        # バンカーが3枚目のカードを引くかどうかを決定 
        elif self.calculate_hand_value(self.gameMaster.handOfCards) <= 2: 
            self.gameMaster.drowCard(self.playingCard.drowCard())
        elif self.calculate_hand_value(self.gameMaster.handOfCards) == 3 and not(self.calculate_hand_value(self.player.handOfCards) == 8):
            self.gameMaster.drowCard(self.playingCard.drowCard())
        elif self.calculate_hand_value(self.gameMaster.handOfCards) == 4 and self.calculate_hand_value(self.player.handOfCards) >= 2 and self.calculate_hand_value(self.player.handOfCards) <= 7:
            self.gameMaster.drowCard(self.playingCard.drowCard())
        elif self.calculate_hand_value(self.gameMaster.handOfCards) == 5 and self.calculate_hand_value(self.player.handOfCards) >= 4 and self.calculate_hand_value(self.player.handOfCards) <= 7:
            self.gameMaster.drowCard(self.playingCard.drowCard())
        elif self.calculate_hand_value(self.gameMaster.handOfCards) == 6 and self.calculate_hand_value(self.player.handOfCards) >= 6 and self.calculate_hand_value(self.player.handOfCards) <= 7:
            self.gameMaster.drowCard(self.playingCard.drowCard())
        # どちらかが8または9に達した場合、ゲーム終了 
        elif self.calculate_hand_value(self.player.handOfCards) >= 8 or self.calculate_hand_value(self.gameMaster.handOfCards) >= 8:
            isDrow = False
        elif self.calculate_hand_value(self.player.handOfCards) >= 6 and self.calculate_hand_value(self.gameMaster.handOfCards) >= 6: 
            isDrow = False
        return isDrow

    def duel(self):
        status = ""
        if self.calculate_hand_value(self.player.handOfCards) > self.calculate_hand_value(self.gameMaster.handOfCards):
            status = "player" 
            print("プレイヤーの勝利！") 
        elif self.calculate_hand_value(self.player.handOfCards) < self.calculate_hand_value(self.gameMaster.handOfCards):
            status = "baccarat.gameMaster"
            print("バンカーの勝利！") 
        else: 
            status = "drow"
            print("引き分け！")
        return status

    def returnChip(self,status,val):
        if status == val:
            if val == "Drow":
                print(str(int(self.betedChip)*9),"枚ゲット")
                self.player.addchip(int(self.betedChip)*9)
            else:
                print(str(int(self.betedChip)*2),"枚ゲット")
                self.player.addchip(int(self.betedChip)*2)
        else:
            print(str(int(self.betedChip)*0),"枚ゲット")

    def showField(self):
        # プレイヤーとバンカーのカードと合計値を表示 
        print("プレイヤーのカード:",end=' ')
        self.player.showHandOfCards() 
        print("合計:", self.calculate_hand_value(self.player.handOfCards))
        print("バンカーのカード:",end=' ')
        self.gameMaster.showAllHandOfCards() 
        print("合計:", self.calculate_hand_value(self.gameMaster.handOfCards)) 