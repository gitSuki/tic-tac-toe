import random

class Game():
    def __init__(self):
        self.welcome()
        self.get_usernames()
        self.first_turn_randomize()
        self.gameboard()
    def __repr__(self):
        pass

    #Prints Welcome Message
    def welcome(self):
        print("Welcome to Tic-Tac-Toe!")
        print("")
        print("Written by gitSuki in Python 3.8.10")
        print("")
        print("")

    #Asks user to input usernames which are assigned to variables
    def get_usernames(self):
        print("Please input Player 1's name:")
        player_1_name = input()
        print("")
        print("Please input Player 2's name:")
        player_2_name = input()
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        print("")

    #Randomizes who gets the first turn
    def first_turn_randomize(self):
        player_1 = 1
        player_2 = 2
        order = random.choices([player_1, player_2])
        self.player_order = order
        print (f"Player {self.player_order} will go first!")

    def gameboard(self):
        print('''
         1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9
        ''')

game = Game()