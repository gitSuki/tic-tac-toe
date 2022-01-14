import random

class Game():
    def __init__(self):
        self.welcome()
        self.get_usernames()
        self.first_turn_randomize()
        self.create_gameboard()
        self.turn()
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
        print("Please input Player 1's name: (The order will be randomized before the game begins)")
        player_1_name = input()
        print("")
        print("Please input Player 2's name:")
        player_2_name = input()
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_names = [self.player_1_name, self.player_2_name]
        print("")

    #Randomizes who gets the first turn
    def first_turn_randomize(self):
        self.order = random.randint(1, 2)
        self.players_dict = dict(zip([1, 2], self.player_names))
        # print(self.players_dict)
        # print(self.order)
        print (f"{self.players_dict[self.order]} (Player {self.order}) will go first!")

    def create_gameboard(self):
        self.board = '''
         1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9
        '''
        print(self.board)

    turn_count = 0
    def turn(self):
        self.turn_count += 1
        print(f"Turn {self.turn_count}: Please input a number (1-9) to claim a location on the gameboard grid.")

game = Game()