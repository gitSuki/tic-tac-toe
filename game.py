import random

class Game():
    def __init__(self):
        pass
    def __repr__(self):
        pass

    #Prints Welcome Message
    def welcome(self):
        print("Welcome to Tic-Tac-Toe!")
        print("")
        print("Written by gitSuki in Python 3.8.10")
        print("")

    #Gets username
    def get_username(self):
        return

    #Randomizes who gets the first turn
    def first_turn_randomize(self):
        player = 1
        ai = 0
        return random.choices([player, ai])

    def gameboard(self):
        print('''
         1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9
        ''')

game = Game()