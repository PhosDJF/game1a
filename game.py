"""what are the stages:
1) setup the board
2) decide who goes first
3) players take turns putting their marker down
4) the game is won when a "connect 3" is achieved
5) the game ends with a draw if all space is used before a winner is deterimined
6) reset the board and start again (maybe keep a log of the scores)

TODO:
 - actually end the game when it is won
 - return the result from the start_game method
 - store this is the main program, or a super-game class
 - add more comunication about what the AI is doing
 -  could throw in some amusing one-liners comentating the ai thinking
 - consider re doing the "player" so they are a class - easier to access things about them
 - more thorough testing of wierd things - make tit so the game doesn't fall over too easily
    - work around wierd inputs from the human for example
- seems to break after the human tries an invalid location, then a good one


"""
import board
import random

from  helpers import linebreak 

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
        possible_moved = self.game_board.find_legal_moves()

        return random.choice(possible_moved)

    def ask_human_for_move(self):

        print(linebreak)
        print("see the current state:")
        self.game_board.show()

        row = int(input("Which row?: "))

        column = int(input("Which column?: "))

        if self.game_board.check_legal_move([row, column]):

            return [row, column]

        else:
            print('Sorry, not a legal move, try again')
            print('the legal moves are: {}'.format(self.game_board.find_legal_moves()))
            self.ask_human_for_move()

    def take_turn(self, player_kind, player):

        # get the move
        if player_kind == 'human':

            location = self.ask_human_for_move()

        else:

            location = self.ai_choice()

        # put the move on the board
        self.game_board.set_grid_value(location, player)

        # has the game ended?
        victory_condition = self.game_board.check_for_victory()
        if victory_condition[0] == True:
            #the game has been won
            print("game won by {}".format(victory_condition[1]))


        elif len(self.game_board.find_legal_moves()) ==0:
            # no more legal moves
            # so it is a draw
            print("the game is a draw")

        else:
            return 

    def start_game(self):

        player_kind_first = self.decide_who_first()
        player_kind_second = [a for a in self.player_kinds if not a== player_kind_first][0]

        print('the first player will be {}'.format(player_kind_first))

        player1 = self.first_player

        player2 = self.second_player

        while True:

            #player1
            self.take_turn(player_kind_first, player1)

            #players
            self.take_turn(player_kind_second, player2)






