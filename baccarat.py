import random
from cardList import cardList
from player import player

# カードの値を計算する関数
def calculate_hand_value(hand):
    sum = 0
    for card in hand:
        if card.number < 10:
            sum += card.number
    return sum%10

# ルール
# 賭けるチップ枚数を決める
# 賭ける場所を決める　Player?orBankerorDrow
# PlayerとBankerにカードを2枚配る
# 条件に応じてカードを配る
# 勝者を決めて、配当を得る　勝者を当てたら賭けたチップ２倍　Drow当てたら9倍

while True:
    # カードデッキを初期化
    deck = cardList()
    deck.unit()
    deck.shuffleCardDeck()
    # 初期のカードをプレイヤーとバンカーに配る 
    player1 = player()
    player1.chip = 10000
    for i in range(2):
        player1.drowCard(deck.drowCard())
    banker = player()
    for i in range(2):
        banker.drowCard(deck.drowCard())
    print("現在のプレイヤーのチップ数: ",str(player1.chip),"枚")
    bet = input('How many chips do you want to bet?: ')
    isChip = player1.betChip(int(bet))
    if not isChip:
        break
    val = input('Where do you bet?(player or banker or drow): ')
    # ゲームのループ 
    while True: 
        # プレイヤーとバンカーのカードと合計値を表示 
        print("プレイヤーのカード:",end=' ')
        player1.showHandOfCards() 
        print("合計:", calculate_hand_value(player1.handOfCards))
        print("バンカーのカード:",end=' ')
        banker.showHandOfCards() 
        print("合計:", calculate_hand_value(banker.handOfCards)) 
        # プレイヤーが3枚目のカードを引くかどうかを決定 
        if calculate_hand_value(player1.handOfCards) <= 5: 
            player1.drowCard(deck.drowCard()) 
        # バンカーが3枚目のカードを引くかどうかを決定 
        elif calculate_hand_value(banker.handOfCards) <= 2: 
            banker.drowCard(deck.drowCard())
        elif calculate_hand_value(banker.handOfCards) == 3 and not(calculate_hand_value(player1.handOfCards) == 8):
            banker.drowCard(deck.drowCard())
        elif calculate_hand_value(banker.handOfCards) == 4 and calculate_hand_value(player1.handOfCards) >= 2 and calculate_hand_value(player1.handOfCards) <= 7:
            banker.drowCard(deck.drowCard())
        elif calculate_hand_value(banker.handOfCards) == 5 and calculate_hand_value(player1.handOfCards) >= 4 and calculate_hand_value(player1.handOfCards) <= 7:
            banker.drowCard(deck.drowCard())
        elif calculate_hand_value(banker.handOfCards) == 6 and calculate_hand_value(player1.handOfCards) >= 6 and calculate_hand_value(player1.handOfCards) <= 7:
            banker.drowCard(deck.drowCard())
        # どちらかが8または9に達した場合、ゲーム終了 
        elif calculate_hand_value(player1.handOfCards) >= 8 or calculate_hand_value(banker.handOfCards) >= 8:
            break
        elif calculate_hand_value(player1.handOfCards) >= 6 and calculate_hand_value(banker.handOfCards) >= 6: 
            break
    # 勝者を判定 
    status = ""
    if calculate_hand_value(player1.handOfCards) > calculate_hand_value(banker.handOfCards):
        status = "player" 
        print("プレイヤーの勝利！") 
    elif calculate_hand_value(player1.handOfCards) < calculate_hand_value(banker.handOfCards):
        status = "banker"
        print("バンカーの勝利！") 
    else: 
        status = "drow"
        print("引き分け！")

    if status == val:
        if val == "Drow":
            print(str(int(bet)*9),"枚ゲット")
            player1.addchip(int(bet)*9)
        else:
            print(str(int(bet)*2),"枚ゲット")
            player1.addchip(int(bet)*2)
    else:
        print(str(int(bet)*0),"枚ゲット")
