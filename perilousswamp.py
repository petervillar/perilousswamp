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


def slow_print(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)


"""
main()
getPlayerMove()
displayMap()
"""


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

def displayMap():
    pass

def getPlayerMove():
    slow_print('''Which way now? - N, S, E, W, OR SE, NW
    etc or "MAP"''')
    print('\n')
    playerMove = input(">>> ").upper().strip()

    return playerMove


def main():
    """Runs a single game of Perilous Swamps"""
    displayCredits()

    while True:
        displayMap()
        playerMove = getPlayerMove()

        if playerMove == "OUT":
            slow_print("So long... better luck next time!")
            print("\n")
            sys.exit()


if __name__ == "__main__":
    main()
