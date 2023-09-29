from Field import Field

def main():
    blackJack = Field()
    blackJack.unit()
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
    blackJack.duel()

if __name__ == '__main__':
    main()