import random

class Game:
    turn_count = 0
    game_state = True
    def __init__(self):
        self.welcome()
        self.get_usernames()
        self.first_turn_randomize()
        self.create_gameboard()
        self.game_loop()

    def __repr__(self):
        pass

    def welcome(self):
        print("Welcome to Tic-Tac-Toe!")
        print("")
        print("Written by gitSuki in Python 3.8.10")
        print("")
        print("")

    def get_usernames(self):
        #Asks user to input usernames which are assigned to variables
        print("Please input Player 1's name: (The order will be randomized before the game begins)")
        player_1_name = input()
        print("")
        print("Please input Player 2's name:")
        player_2_name = input()
        self.player1 = Player(player_1_name, 1, "X")
        self.player2 = Player(player_2_name, 2, "O")
        print("")
        print("")

    def first_turn_randomize(self):
        #Randomizes who gets the first turn
        randomized_order = random.randint(1, 2)
        if randomized_order == 2:
            self.player1.order = 2
            self.player1.order = 1        
            self.players_dict = dict(zip([1, 2], [self.player2, self.player1]))
        else: self.players_dict = dict(zip([1, 2], [self.player1, self.player2]))
        print (f"{self.players_dict[1].name} (Player {randomized_order}) will go first!")

    def create_gameboard(self):
        self.board = '''
         1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9
        '''
        print(self.board)

    def game_loop(self):
        while self.turn_count < 9 and self.game_state:
            #If turn count is odd (starting from 0), the player who was randomized to go first goes
            if self.turn_count % 2 == 0:
                Turn(self, self.players_dict[1])
            #Otherwise, the player who was randomized to go second goes
            else:
                Turn(self, self.players_dict[2])
        else:
            if self.game_state == True:
                self.game_over(True)
            else: pass

    def game_over(self, tie, player_name = None, player_order = None):
        #Prints a victory message asks the player and calls the continue method
        if tie == True:
            print(f"The game was a tie!")
            self.ask_to_continue()
        else:
            print(f"Congratulations! {player_name} (Player {str(player_order)}) won!")
            self.ask_to_continue()
        
    def ask_to_continue(self):
        #Asks the player if they'd like to play another round
        print('')
        print("Would you like to play again?")
        print('Type "Y" if you would like to play another game, otherwise type "N"')
        continue_input = input()
        if continue_input == "N" or continue_input == "n":
            self.game_state = False
        elif continue_input == "Y" or continue_input == "y":
            print('')
            Game()


class Player:
    def __init__(self, name, order, user_mark):
        self.name = name
        self.order = order
        self.mark = user_mark


class Turn:
    def __init__(self, game, player):
        #Grabs the relevant values from the Player and Game classes
        self.game = game
        self.player = player
        self.turn_count = game.turn_count
        self.board = game.board
        self.run_turn()
    
    def counter(self):
        #Updates the counter within both the Turn and Game classes
        self.turn_count += 1
        self.game.turn_count = self.turn_count
        print(f"Turn {self.turn_count}: Please input a number (1-9) to claim a location on the gameboard grid.")

    def user_input(self):
        #Loops until the user gives a valid input that can be replaced on the gameboard
        while True:
            user_input = input()
            if len(user_input) != 1 or user_input not in self.board or user_input.isnumeric() == False:
                print ("Error - invalid input. Please try again with a valid number:")
                print("")
                continue
            else:
                break
        self.user_input = user_input

    def alter_gameboard(self):
        #Replaces the existing numbers on the gameboard with the user's mark
        self.new_board = self.board.replace(self.user_input, self.player.mark)
        print(self.new_board)
        self.game.board = self.new_board

    def filter_gameboard(self):
        #Filters through the gameboard and makes a list including only the remaining digits and player numbers
        self.filter_list = ["X", "O", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.filtered_gameboard = []
        for entry in list(self.game.board):
            if entry in self.filter_list:
                self.filtered_gameboard.append(entry)

    def check_victory(self):
        #Horizontal Victory
        if all(entry == self.player.mark for entry in self.filtered_gameboard[:3]) or \
            all(entry == self.player.mark for entry in self.filtered_gameboard[3:6]) or \
            all(entry == self.player.mark for entry in self.filtered_gameboard[6:]):
                self.game.game_over(False, self.player.name, self.player.order)
        #Vertical Victory
        elif all(entry == self.player.mark for entry in self.filtered_gameboard[::3]) or \
            all(entry == self.player.mark for entry in self.filtered_gameboard[1::3]) or \
            all(entry == self.player.mark for entry in self.filtered_gameboard[2::3]):
                self.game.game_over(False, self.player.name, self.player.order)        
        #Diagonal Victory
        elif all(entry == self.player.mark for entry in [self.filtered_gameboard[0], self.filtered_gameboard[4], self.filtered_gameboard[8]]) or all(entry == self.player.mark for entry in [self.filtered_gameboard[2], self.filtered_gameboard[4], self.filtered_gameboard[6]]):
                self.game.game_over(False, self.player.name, self.player.order)
        else: pass

    def run_turn(self):
        #Runs through the Turn class methods
        print(f"The player is {self.player.name} (Player {str(self.player.order)})")
        self.counter()
        self.user_input()
        self.alter_gameboard()
        self.filter_gameboard()
        self.check_victory()


game = Game()