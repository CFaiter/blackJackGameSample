from Field import Field

def main():
    blackJack = Field()
    while True:
        blackJack.unit()
        playerBetChip = blackJack.callBetChip()
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
        blackJack.returnChip(status,playerBetChip)

if __name__ == '__main__':
    main()