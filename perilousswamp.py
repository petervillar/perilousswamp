"""Perilous Swamps from Fantasy Games
http://www.zx81stuff.org.uk/zx81/tape/FantasyGames"""

import sys
import time
from os import system, name


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
        ["#", ".", ".", "X", " ", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", " ", ".", ".", ".", ".", ".", ".", "#"],
        ["#", " ", ".", " ", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", " ", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", " ", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", " ", " ", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", " ", ".", "#"],
        ["#", ".", ".", ".", ".", ".", "*", " ", " ", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]

    gubbe = [1, 3]
    princess = (9, 6)

    swampMap[gubbe[0]][gubbe[1]] = "X"
    swampMap[princess[0]][princess[1]] = "*"

    return swampMap, gubbe, princess


def displayMap(swampMap):
    print(" N")
    print("W+E\tX = You, * = Princess, . = swamp, # = edge")
    print(" S \t. = swamp, # = edge")
    print()

    for row in swampMap:
        print(*row, sep="")

def movePlayer(gubbe, playerMove, swampMap):
    if playerMove == "N":
        northOfGubbe = gubbe[0] - 1
        thingNorthOfGubbe = swampMap[northOfGubbe][gubbe[1]]
        if thingNorthOfGubbe != "#":
            gubbe[0] = northOfGubbe
        elif thingNorthOfGubbe == "#":
            endGame()

def endGame():
    print("You survived the swamp with % skill and % luck.")
    print("You ripped off a total of % treasure points off the poor overworked monsters.")
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

    gubbe = ()
    princess = ()
    swampMap, gubbe, princess = initializeMap()

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

        elif playerMove in ["N", "S", "E", "W", "NE", "NW", "SE", "SE"]:
            movePlayer(gubbe, playerMove, swampMap)

        else:
            continue


if __name__ == "__main__":
    main()
