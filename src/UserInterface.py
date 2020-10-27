import Deck
import Menu


class UserInterface:
    def __init__(self):
        pass

    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
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
        # TODO: Get the user to specify the card size, max number, and number of cards
        print("Enter card size [3 - 15]")
        cardSize = int(input())
        while not cardSize in range(3, 15):
            print(f"{cardSize} is not between [3 - 15]\n Please Re Enter a valid number:")
            cardSize = int(input())
        self.__cardSize = cardSize
        print("Enter max number [50 - 100]")
        maxNumber = int(input())
        while not maxNumber in range(50, 100):
            print(f"{maxNumber} is not between [50 - 100]\n Please Re Enter a valid number:")
            maxNumber = int(input())
        self.__maxNumber = maxNumber
        print("Enter number of cards [3 - 10000]")
        deckSize = int(input())
        while not deckSize in range(3, 10000):
            print(f"{cardSize} is not between [3 - 10000]\n Please Re Enter a valid number:")
            deckSize = int(input())
        self.deckSize = deckSize

        self.__m_currentDeck = Deck.Deck(self.__cardSize, self.deckSize, self.__maxNumber)
        self.__deckMenu()

    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
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
        print(f"{printST} [{minV} - {maxV}]")
        return int(input())

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
