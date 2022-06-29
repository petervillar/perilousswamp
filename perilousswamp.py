"""Perilous Swamps from Fantasy Games
http://www.zx81stuff.org.uk/zx81/tape/FantasyGames"""

import sys
import time
from os import system, name

SWAMP = "·"
EDGE = "#"
YOU = "X"
PRINCESS = "*"


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def displayCredits():
    clear()

    print(
        """
                    ==============
                    Perilous Swamp
                    =============="""
    )

    print(
        """
    In this game, you find yourself in a swampy forest.
    Your task is to find your way to the edge alive, and
    with as much treasure as possible.

    A beautiful princess is held by an evil wizard. The king
    wouldn't mind if you could release her...

    Should you have to leave early, typing "out" should get you
    out - permanently."""
    )

    print("\n\n")
    input("To start press the enter key...")
    print("\n")


def getPlayerMove():
    print(
        '''Which way now? - N, S, E, W, OR SE, NW
    etc, "MAP" or "OUT"'''
    )
    print("\n")
    playerMove = input(">>> ").upper().strip()

    return playerMove


def initializeMap():
    swampMap = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "·", " ", "X", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "·", "·", " ", "·", "·", "·", " ", " ", "·", "#"],
        ["#", "·", "·", " ", "·", "·", "·", " ", " ", " ", "#"],
        ["#", "·", " ", "·", "·", " ", "·", " ", " ", " ", "#"],
        ["#", "·", "·", " ", " ", " ", " ", " ", "·", "·", "#"],
        ["#", " ", "·", "·", "·", "·", "·", " ", "·", "·", "#"],
        ["#", "·", "·", " ", "·", " ", "·", "·", " ", "·", "#"],
        ["#", " ", " ", "·", " ", "·", " ", "·", "·", " ", "#"],
        ["#", " ", "·", "·", " ", " ", " ", "·", " ", "·", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]

    playerPosition = [1, 3]
    princessPosition = (6, 5)

    swampMap[playerPosition[0]][playerPosition[1]] = YOU
    swampMap[princessPosition[0]][princessPosition[1]] = PRINCESS

    return swampMap, playerPosition, princessPosition


def updateMap(swampMap, oldPlayerPosition, playerPosition, princessPosition):
    swampMap[oldPlayerPosition[0]][oldPlayerPosition[1]] = " "
    swampMap[playerPosition[0]][playerPosition[1]] = "X"
    swampMap[princessPosition[0]][princessPosition[1]] = "*"

    return swampMap


def displayMap(swampMap):
    print(" N")
    print("W+E\tX = You, * = Princess, · = swamp, # = edge")
    print(" S ")
    print()

    for row in swampMap:
        print(*row, sep="")


def movePlayer(playerPosition, playerMove, swampMap):
    oldPlayerPosition = playerPosition.copy()

    if playerMove == "N":
        playerPosition[0] = playerPosition[0] - 1
    elif playerMove == "S":
        playerPosition[0] = playerPosition[0] + 1
    elif playerMove == "E":
        playerPosition[1] = playerPosition[1] + 1
    elif playerMove == "W":
        playerPosition[1] = playerPosition[1] - 1
    elif playerMove == "NE":
        playerPosition[0] = playerPosition[0] - 1
        playerPosition[1] = playerPosition[1] + 1
    elif playerMove == "NW":
        playerPosition[0] = playerPosition[0] - 1
        playerPosition[1] = playerPosition[1] - 1
    elif playerMove == "SE":
        playerPosition[0] = playerPosition[0] + 1
        playerPosition[1] = playerPosition[1] + 1
    elif playerMove == "SW":
        playerPosition[0] = playerPosition[0] + 1
        playerPosition[1] = playerPosition[1] - 1

    thingPlayerPosition = swampMap[playerPosition[0]][playerPosition[1]]
    if thingPlayerPosition == EDGE:
        endGame()
    elif thingPlayerPosition == SWAMP:
        print("Too wet that way, clot.\n")
        playerPosition = oldPlayerPosition

    return playerPosition


def endGame():
    print("You survived the swamp with % skill and % luck.")
    print(
        "You ripped off a total of % treasure points off the poor overworked monsters."
    )
    print("% of them died protecting their rightful treasure.")
    print("\nCongratulations!\n")
    print("Pity about the princess...")
    print("The wizard fed her to a dragon.")
    print("The king is not at all that pleased.")
    print("\nTry again?... You could get lucky.")

    sys.exit()


def main():
    """Runs a single game of Perilous Swamps"""
    displayCredits()
    clear()

    playerPosition = []
    princessPosition = ()
    swampMap, playerPosition, princessPosition = initializeMap()

    displayMap(swampMap)
    print()

    while True:
        playerMove = getPlayerMove()

        if playerMove == "OUT":
            print("So long... better luck next time!")
            print("\n")
            sys.exit()

        elif playerMove == "MAP":
            clear()
            displayMap(swampMap)

        elif playerMove in ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]:
            oldPlayerPosition = playerPosition.copy()
            playerPosition = movePlayer(playerPosition, playerMove, swampMap)
            swampMap = updateMap(
                swampMap, oldPlayerPosition, playerPosition, princessPosition
            )

        else:
            continue


if __name__ == "__main__":
    main()
