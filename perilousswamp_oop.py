"""Perilous Swamps from Fantasy Games
http://www.zx81stuff.org.uk/zx81/tape/FantasyGames"""

import sys
import time
from os import system, name

SWAMP = "·"
EDGE = "#"
YOU = "X"
PRINCE = "*"

class Player:
    def __init__(self):
        self.skill = 0
        self.luck = 0
        self.treasurePoints = 0
        self.killedMonsters = 0
        self.playerPos = [1, 3]


class PerilousSwampBoard:
    def __init__(self, playerPos):
        self.playerPos = playerPos

        # TODO: randomize
        self.princePos = (6, 5)
        self.swampMap = [
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
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ]

        self.swampMap[self.playerPos[0]][self.playerPos[1]] = YOU
        self.swampMap[self.princePos[0]][self.princePos[1]] = PRINCE

    def updateMap(self, swampMap, oldPlayerPosition, playerPosition, princessPosition):
        swampMap[oldPlayerPosition[0]][oldPlayerPosition[1]] = " "
        swampMap[playerPosition[0]][playerPosition[1]] = "X"
        swampMap[princessPosition[0]][princessPosition[1]] = "*"

        return swampMap

    def displayMap(self):
        print(" N")
        print("W+E\tX = You, * = Prince, · = swamp, # = edge")
        print(" S ")
        print()
        for row in self.swampMap:
            print(*row, sep="")
        print()

    def movePlayer(self, playerMove):
        tmpPlayerPos = self.playerPos.copy()
        print(tmpPlayerPos)

        if playerMove == "N":
            tmpPlayerPos[0] = tmpPlayerPos[0] - 1
        elif playerMove == "S":
            tmpPlayerPos[0] = tmpPlayerPos[0] + 1
        elif playerMove == "E":
            tmpPlayerPos[1] = tmpPlayerPos[1] + 1
        elif playerMove == "W":
            tmpPlayerPos[1] = tmpPlayerPos[1] - 1
        elif playerMove == "NE":
            tmpPlayerPos[0] = tmpPlayerPos[0] - 1
            tmpPlayerPos[1] = tmpPlayerPos[1] + 1
        elif playerMove == "NW":
            tmpPlayerPos[0] = tmpPlayerPos[0] - 1
            tmpPlayerPos[1] = tmpPlayerPos[1] - 1
        elif playerMove == "SE":
            tmpPlayerPos[0] = tmpPlayerPos[0] + 1
            tmpPlayerPos[1] = tmpPlayerPos[1] + 1
        elif playerMove == "SW":
            tmpPlayerPos[0] = tmpPlayerPos[0] + 1
            tmpPlayerPos[1] = tmpPlayerPos[1] - 1

        print(tmpPlayerPos)
        thingPlayerPos = self.swampMap[tmpPlayerPos[0]][tmpPlayerPos[1]]

        if thingPlayerPos == EDGE:
            endGame()
        elif thingPlayerPos == SWAMP:
            print("Too wet that way, clot.\n")
        else:
            self.playerPos = tmpPlayerPos.copy()

def clearScreen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def displayCredits():

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

    A handsome prince is held by an evil wizard. The queen
    wouldn't mind if you could release him...

    Should you have to leave early, typing "out" should get you
    out - permanently."""
    )

    print("\n\n")
    input("To start press the enter key...")
    print("\n")

def endGame():
    print("You survived the swamp with % skill and % luck.")
    print(
        "You ripped off a total of % treasure points off the poor overworked monsters."
    )
    print("% of them died protecting their rightful treasure.")
    print("\nCongratulations!\n")
    print("Pity about the prince...")
    print("The wizard fed her to a dragon.")
    print("The king is not at all that pleased.")
    print("\nTry again?... You could get lucky.")

    sys.exit()

def getPlayerMove():
    print(
        '''Which way now? - N, S, E, W, OR SE, NW
    etc, "MAP" or "OUT"'''
    )
    print("\n")
    playerMove = input(">>> ").upper().strip()

    return playerMove

def main():
    """Runs a single game of Perilous Swamps"""
    clearScreen()
    displayCredits()
    clearScreen()

    player = Player()
    swampMap = PerilousSwampBoard(player.playerPos)
    swampMap.displayMap()

    while True:
        playerMove = getPlayerMove()

        if playerMove == "OUT":
            print("So long... better luck next time!")
            print("\n")
            sys.exit()

        elif playerMove == "MAP":
            clearScreen()
            swampMap.displayMap()

        elif playerMove in ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]:
#            oldPlayerPos = playerPos.copy()
#            playerPosition = swampMap.movePlayer(playerPosition, playerMove)
#            swampMap = updateMap(
#                swampMap, oldPlayerPosition, playerPosition, princessPosition
#            )
            swampMap.movePlayer(playerMove)

        else:
            continue


if __name__ == "__main__":
    main()
