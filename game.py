import random

class Game:
    turn_count = 0
    def __init__(self):
        self.welcome()
        self.get_usernames()
        self.first_turn_randomize()
        self.create_gameboard()
        Turn(self)

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
        player1 = Player(player_1_name)
        player2 = Player(player_2_name)
        self.player_names = [player1.name, player2.name]
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

class Player:
    def __init__(self, name,):
        self.name = name


class Turn:
    def __init__(self, game):
        self.game = game
        self.turn_count = game.turn_count
        self.board = game.board
        self.turn()
    
    def counter(self):
        self.turn_count += 1
        print(f"Turn {self.turn_count}: Please input a number (1-9) to claim a location on the gameboard grid.")
        print("")

    def user_input(self):
        while True:
            user_input = input()
            if len(user_input) != 1 or user_input not in self.board or user_input.isnumeric() == False:
                print ("Error - invalid input. Please try again with a valid number:")
                print("")
                continue
            else:
                break
        self.user_input = user_input
        print("Input was " + self.user_input)

    def alter_gameboard(self):
        self.new_board = self.board.replace(self.user_input, "X")
        print(self.new_board)
        self.game.board = self.new_board
        
    def turn(self):
        self.counter()
        print("Player 1 is " + self.game.players_dict[1])
        self.user_input()
        self.alter_gameboard()

game = Game()