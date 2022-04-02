"""what are the stages:
1) setup the board
2) decide who goes first
3) players take turns putting their marker down
4) the game is won when a "connect 3" is achieved
5) the game ends with a draw if all space is used before a winner is deterimined
6) reset the board and start again (maybe keep a log of the scores)

"""
import board
import random

class game():

    def __init__(self):
        #not sure if will be needed
        self.game_board = board.board()
        self.first_player = self.game_board.players[0]
        self.second_player = self.game_board.players[1]

        self.player_kinds = ['human', 'ai']

    def decide_who_first(self):
        #start by hardcoing as the human
        return self.player_kinds[0]


    def ai_choice(self):

        # randomly make a legal move
        possible_moved = self.game_board.find_legal_moves(self)

        return random.choice(possible_moved)

    def ask_human_for_move(self):

        row = input("Which row?: ")

        column = input("Which column?: ")

        if self.game_board.check_legal_move([row, column]):

            return [row, column]

        else:
            print('Sorry, not a legal move, try again')
            print('the legal moves are: {}'.format(self.game_board.find_legal_moves()))
            self.ask_human_for_move(self)

    def take_turn(self, player_kind, player):

        # get the move
        if player_kind == 'human':

            location = self.ask_human_for_move()

        else:

            location = self.ai_choice()

        # put the move on the board
        self.game_board.set_grid_value(location, player)

        # has the game ended?
        if False:
            #the game has been won
            pass

        elif len(self.game_board.find_legal_moves()) ==0:
            # no more legal moves
            # so it is a draw



