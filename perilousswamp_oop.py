"""Perilous Swamps from Fantasy Games
http://www.zx81stuff.org.uk/zx81/tape/FantasyGames"""

import textwrap
import sys
import time
import random
from os import system, name

SWAMP = "·"
EDGE = "#"
YOU = "X"
PRINCE = "*"


class SwampPlayer:
    def __init__(self):
        self.skill = 0
        self.combatStrength = random.randint(1500, 2000)
        self.luck = 0
        self.treasurePoints = 0
        self.killedMonsters = 0


class SwampBoard:
    def __init__(self):
        # TODO: randomize
        self.playerPos = [1, 3]
        self.tmpPlayerPos = self.playerPos.copy()
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
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ]

        self.swampMap[self.playerPos[0]][self.playerPos[1]] = YOU
        self.swampMap[self.princePos[0]][self.princePos[1]] = PRINCE

    def updateMap(self):
        self.swampMap[self.oldPlayerPos[0]][self.oldPlayerPos[1]] = " "
        self.swampMap[self.playerPos[0]][self.playerPos[1]] = "X"
        self.swampMap[self.princePos[0]][self.princePos[1]] = "*"

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

        thingPlayerPos = self.swampMap[tmpPlayerPos[0]][tmpPlayerPos[1]]

        if thingPlayerPos == EDGE:
            endGame()
        elif thingPlayerPos == SWAMP:
            print("Too wet that way, clot.\n")
        else:
            self.oldPlayerPos = self.playerPos.copy()
            self.playerPos = tmpPlayerPos.copy()


class SwampMonster:
    def __init__(self):
        self.type = random.choice(
            [
                "nothing",
                "werewolf",
                "bunyip",
                "phoenix",
                "troll",
                "goblin",
                "giant",
                "gorgon",
                "dragon",
                "ogre",
                "wizard",
            ]
        )
        self.description = random.choice(
            [
                "fiendish",
                "green",
                "foul",
                "slimy",
                "tough",
                "horrible",
                "hungry",
                "nasty",
                "dirty",
            ]
        )
        self.treasures = random.choice(
            [
                ["10 silver spoons", 10],
                ["a jewelled sword", 30],
                ["a jar of rubies", 50],
                ["a treasure chest", 200],
                ["50 silver pieces", 50],
                ["100 gold pieces", 100],
                ["a box of jewels", 75],
                ["a fair princess", 1],
            ]
        )

        self.combatStrength = random.randint(20, 100)


def swampEncounter(player, monster):
    """ Combat scenes are made up, couldn't bother looking at the BASIC source"""
    print(f"Your combat strength is {player.combatStrength}")
    print(f"A {monster.description} {monster.type} is guarding {monster.treasures[0]}")
    print(f"Its combat points come to {monster.combatStrength}")

    action = input("Do you wish to-\nFight, Run, or Bribe? ").upper()[0]

    if action == "R":
        time.sleep(0.4)
        if random.randint(0, 100) < 60:
            print("\nBut not fast enough...")
            print("\nNow you can only fight.")
            action = "F"
        else:
            print("\nYou sure run fast if you need to!\n")
            return

    if action == "B":
        pass
    elif action == "F":
        combatPoints = int(input("How many combat points? "))
        deadMsg = textwrap.dedent("""
        Too bad... The monster ate you...
        And took all your treasure...
        Pity about the prince...
        The wizard fed him to a dragon
        The Queen is not all that pleased

        Try again? You could get lucky
        """)

        print(deadMsg)
        sys.exit()

    return


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


def endGame(p):
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
    player = SwampPlayer()
    swampMap = SwampBoard()

    clearScreen()
    displayCredits()
    clearScreen()

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
            swampMap.movePlayer(playerMove)
            swampMap.updateMap()
            monster = SwampMonster()
            swampEncounter(player, monster)

        else:
            continue


if __name__ == "__main__":
    main()
