# Python 3
from os import system, name
from time import sleep
from random import randint

def main():
    # Initialize Cards Array
    cards = ["Q", "Q", "Q", "Q"]
    # Other variables
    shuffleCount = 0
    userScore = 0
    userGames = 0
    playAgain = "y"
    difficulty = welcome(cards)
    if difficulty == 1:
        difficultyShuffles = randint(5,10)
        difficultySleep = .6
    elif difficulty == 2:
        difficultyShuffles = randint(20,25)
        difficultySleep = .4
    elif difficulty == 3:
        difficultyShuffles = randint(30,40)
        difficultySleep = .25
    # Shuffle loop
    while playAgain == "y":
        clearScreen()
        showCards(cards)
        print(" Get ready to play Follow the Queen!" )
        startIn = 5
        while startIn > 0:
            clearScreen()
            showCards(cards)
            print(" Get ready to play Follow the Queen!")
            print(" Starting in " + str(startIn) + "...")
            sleep(1)
            startIn = startIn - 1
        while shuffleCount < difficultyShuffles:
            clearScreen()
            initCards(cards)
            showCards(cards)
            sleep(difficultySleep)
            clearScreen()
            shuffleCount = shuffleCount + 1
        userScore = userScore + checkUserGuess(cards)
        userGames = userGames + 1
        shuffleCount = 0
        if userScore == 0:
            print(" You haven't found the queen yet!")
            playAgain = newGame()
        elif userScore == 1:
            print(" You found the Queen 1 time!")
            playAgain = newGame()
        else:
            print(" You found the Queen " + str(userScore) + " times out of " + str(userGames) + " games!")
            playAgain = newGame()
    clearScreen()
    cards = ["Q", "Q", "Q", "Q"]
    showCards(cards)
    print("\n   You found the queen\n    " + str(round(userScore/userGames*100)) + "% of the time.")
    print("   Thanks for playing!\n ")

def initCards(cards):
    for i, c in enumerate(cards):
        cards[i] = "K"
    queen = randint(0,3)
    cards[queen] = "Q"

def showCards(cards):
    print("  ___   ___   ___   ___  ")
    print(" |   | |   | |   | |   | ")
    print(" | " + cards[0] + " | "
          "| " + cards[1] + " | "
          "| " + cards[2] + " | "
          "| " + cards[3] + " | ")
    print(" |___| |___| |___| |___| ")

def checkUserGuess(cards):
    userGuess = 0
    print("  ___   ___   ___   ___  ")
    print(" |   | |   | |   | |   | ")
    print(" | 1 | | 2 | | 3 | | 4 | ")
    print(" |___| |___| |___| |___| ")
    while userGuess < 1 or userGuess > 4:
        try:
            userGuess = int(input(" Where's the Queen?\n Choose a card: "))
            if userGuess < 1 or userGuess > 4:
                print(" Please choose a card number between 1 and 4!")
        except ValueError:
            userGuess = int(input(" Please choose a card number between 1 and 4!\n Where's the Queen?"))
    clearScreen()
    showCards(cards)
    if cards[int(userGuess-1)] == "Q":
        print(" You picked card number " + str(userGuess) + ".")
        print(" You found the Queen!")
        sleep(1)
        return 1
    else:
        print(" You picked card number " + str(userGuess) + ".")
        print(" That's not the Queen!")
        sleep(1)
        return 0

def newGame():
    playAgain = ""
    while playAgain != "y" and playAgain != "n":
        playAgain = input(" Play again? [Y/n]: ")
        if playAgain == "":
            playAgain = "y"
        playAgain = playAgain.lower()
    if playAgain == "y":
        return "y"
    else:
        return "n"

def welcome(cards):
    clearScreen()
    showCards(cards)
    difficulty = 0
    print("Welcome to Follow the Queen")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    while difficulty < 1 or difficulty > 3:
        try:
            difficulty = int(input("Please select your difficulty: "))
            if difficulty < 1 or difficulty > 3:
                clearScreen()
                showCards(cards)
                print("Welcome to Follow the Queen")
                print("1. Easy")
                print("2. Normal")
                print("3. Hard")
                print("\'" + str(difficulty) + "\' is not a valid difficulty.")
        except ValueError:
            clearScreen()
            showCards(cards)
            print("Welcome to Follow the Queen")
            print("1. Easy")
            print("2. Normal")
            print("3. Hard")
            difficulty = 0
    return difficulty


def clearScreen():
    # Python method for clearing screen found at https://www.geeksforgeeks.org/clear-screen-python/
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For Mac/*nix
    else:
        _ = system('clear')

main()
