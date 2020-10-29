import Deck
import Menu
from colorama import Fore, Style, init

init(convert=True)


class UserInterface:
    def __init__(self):
        pass

    def run(self):
        init()
        print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}Welcome to the Bingo! Deck Generator\n")

        print(
            f"Different Colors indicate different prompts:\n{Fore.LIGHTCYAN_EX}      * Cyan:   Menu\n{Fore.GREEN}      "
            f"* Green:  Asking for User Input\n{Fore.RED}      * Red:    Error{Fore.LIGHTCYAN_EX}")

        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
                pass
            elif command == "X":
                keepGoing = False

    def __createDeck(self):
        # ---------------------- Card Size------------------
        print(f"{Fore.GREEN}Enter card size [3 - 15]")
        try:
            cardSize = int(input())
        except:
            cardSize = 0
        while not cardSize in range(3, 16):
            print()
            print(f"{Fore.RED}Please input a number in the range [3 - 15]")
            print()
            print(f"{Fore.GREEN}Enter card size [3 - 15]")
            try:
                cardSize = int(input())
            except:
                cardSize = 0
        self.__cardSize = cardSize
        # ---------------------- Max Number------------------
        print(f"{Fore.GREEN}Enter max number [{cardSize ** 2 * 2} - {cardSize ** 2 * 4}]")
        try:
            maxNumber = int(input())
        except:
            maxNumber = 0
        while not maxNumber in range(cardSize ** 2 * 2, cardSize ** 2 * 4 + 1):
            print()
            print(f"{Fore.RED}Please input a number in the range [{cardSize ** 2 * 2} - {cardSize ** 2 * 4}]")
            print()
            print(f"{Fore.GREEN}Enter max number [{cardSize ** 2 * 2} - {cardSize ** 2 * 4}]")
            try:
                maxNumber = int(input())
            except:
                maxNumber = 0
        self.__maxNumber = maxNumber
        # ---------------------- Deck Size------------------
        print(f"{Fore.GREEN}Enter number of cards [3 - 10000]")
        try:
            deckSize = int(input())
        except:
            deckSize = 0
        while not deckSize in range(3, 10001):
            print()
            print(f"{Fore.RED}Please input a number in the range [3 - 10000]")
            print()
            print(f"{Fore.GREEN}Enter number of cards [3 - 10000]")
            try:
                deckSize = int(input())
            except:
                deckSize = 0
        print(f"{Fore.LIGHTCYAN_EX}")
        self.deckSize = deckSize

        self.__m_currentDeck = Deck.Deck(self.__cardSize, self.deckSize, self.__maxNumber)
        self.__deckMenu()

    def __deckMenu(self):
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __getNumberInput(self, printST, minV, maxV):
        usrInput = 0
        while usrInput == 0:
            print(f"{printST} [{minV} - {maxV}]")
            try:
                tmpVar = int(input())
                if tmpVar not in range(minV, maxV + 1):
                    print()
                    print(f"{Fore.RED}Please enter a number [{minV} - {maxV}]{Fore.GREEN}")
                    print()
                    continue
                usrInput = tmpVar
            except:
                print()
                print(f"{Fore.RED}Please enter a number [{minV} - {maxV}]{Fore.GREEN}")
                print()
                continue
        return usrInput

    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)

    def __getStringInput(self, strI):
        print(strI)
        return input()

    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name")
        if fileName != "":
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")
