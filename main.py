from Field import Field

def main():
    blackJack = Field()
    blackJack.changeChip(1000)
    while True:
        blackJack.unit()
        blackJack.callBetChip()
        blackJack.showField()
        print()
        # cpu'sのターン
        blackJack.cpuMode()
        # playerのターン
        blackJack.playerMode()
        # gameMasterのターン
        blackJack.gameMasterMode()

        # Duel!
        print("\nDuel!")
        status = blackJack.duel()
        blackJack.returnChip(status)

if __name__ == '__main__':
    main()