from blackJack import blackJack
from baccarat import baccarat

def main():
    while True:
        val = input("which game do you play? blackJack or baccarat: ")
        if val == "blackJack":
            game = blackJack()
            game.changeChip(10000)
            while True:
                game.unit(3)
                game.callBetChip()
                if game.betedChip == 0:
                    print("finish!")
                    break
                game.showField()
                print()
                # cpu'sのターン
                game.cpuMode()
                # playerのターン
                game.playerMode()
                # gameMasterのターン
                game.gameMasterMode()

                # Duel!
                print("\nDuel!")
                status = game.duel()
                game.returnChip(status)
        elif val == "baccarat":
            # gameの流れ
            # 賭けるチップ枚数を決める
            # 賭ける場所を決める　Player?orbaccarat.gameMasterorDrow
            # Playerとbaccarat.gameMasterにカードを2枚配る
            # 条件に応じてカードを配る
            # 勝者を決めて、配当を得る　勝者を当てたら賭けたチップ２倍　Drow当てたら9倍
            game = baccarat()
            game.changeChip(10000)

            while True:
                # カードデッキを初期化
                game.unit(0)
                print("現在のプレイヤーのチップ数: ",str(game.player.chip),"枚")
                game.callBetChip()
                if game.betedChip == 0:
                    print("finish!")
                    break
                val = input('Where do you game.betedChip?(player or game.gameMaster or drow): ')
                # ゲームのループ 
                while True: 
                    game.showField()
                    isDrow = game.judgeDrow()
                    if not isDrow:
                        break
                # 勝者を判定 
                status = game.duel()
                game.returnChip(status,val)
        elif val == "Finish" or val == "finish":
            print("game finish!")
            break

if __name__ == '__main__':
    main()