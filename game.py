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

    #Gets usernames
    def get_usernames(self):
        print("Please input Player 1's Name:")
        player_1_name = input()
        print("Please input Player 2's Name:")
        player_2_name = input()
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name

    #Randomizes who gets the first turn
    def first_turn_randomize(self):
        player_1 = 1
        played_2 = 0
        return random.choices([player_1, player_2])

    def gameboard(self):
        print('''
         1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9
        ''')

game = Game()
game.welcome()
game.get_usernames()