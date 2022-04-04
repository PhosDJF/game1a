"""what are the stages:
1) setup the board
2) decide who goes first
3) players take turns putting their marker down
4) the game is won when a "connect 3" is achieved
5) the game ends with a draw if all space is used before a winner is deterimined
6) reset the board and start again (maybe keep a log of the scores)

TODO:

 - add more comunication about what the AI is doing
 - make communicatoin about the moves human frienly (i.e. not zero-indexed)
 - could throw in some amusing one-liners comentating the ai thinking
 - more thorough testing of wierd things - make it so the game doesn't fall over too easily
    - work around wierd inputs from the human for example
- solved ai isnt working right now, e.g. human moves are - [0.0], [1,0], [1,1], [2,2]

"""
import board
import random
import player
import ai
from  helpers import linebreak 


def try_int_input(text_to_display, legal_range=None):

    if not legal_range is None:

        fail_message = 'invlaid input, expecting an int in {}'.format(legal_range)

    else:

        fail_message = 'invlaid input, expecting an int'

    try:
        response= int(input(text_to_display))

        if not legal_range is None:

            if response in legal_range:
                return response

            else:
                print(fail_message)

            return try_int_input(text_to_display)

        return response

    except:

        print(fail_message)

        return try_int_input(text_to_display)








class game():

    def __init__(self):

        pass
        

    def decide_who_first(self):

        return 'human'
        #TODO make this an option to choose, or be random

    def set_ai(self):

        which_ai=input('Which AI do you want to play with?')

        
        if which_ai=='random':
            self.ai = ai.RandomAI('random ai')

        elif which_ai=='smart':
            self.ai = ai.SlightlySmartAI('smart ai')

        elif which_ai=='solved':
            self.ai = ai.SolvedAI('solved ai')
        
        else:
            
            print('expecting random or smart or solved')

            self.set_ai(self)


    def ask_human_for_move(self):

        print("see the current state:")
        self.game_board.show()

        row = try_int_input("Which row?: ", legal_range=range(1,4))-1

        column = try_int_input("Which column?: ", legal_range=range(1,4))-1

        if self.game_board.check_legal_move([row, column]):

            return [row, column]

        else:
            print('Sorry, not a legal move, try again')
            print('the legal moves are: {}'.format(self.game_board.find_legal_moves()))
            return self.ask_human_for_move()

    def take_turn(self, player, opponent):

        # get the move
        if player.kind == 'human':

            location = self.ask_human_for_move()
            print('doing the move {}'.format(location))

        else:
            print("see the current state:")
            self.game_board.show()
            location = self.ai.decide_move(self.game_board, player, opponent)
            print('doing the move {}'.format(location))

        # put the move on the board
        self.game_board.set_grid_value(location, player.marker)

        # has the game ended?
        if self.game_board.check_for_victory() == True:
            #the game has been won
            print("game won by {}".format(player.kind))
            print('This was the final position:')
            self.game_board.show()

            return True


        elif self.game_board.check_for_full_board() == True:
            # no more legal moves
            # so it is a draw
            print("the game is a draw")
            print('This was the final position:')
            self.game_board.show()

            return False

        else:
            return None

    def start_game(self):

        

        player1 = player.Player()

        player2 = player.Player()


        player1.set_type('human')
        player1.set_team('nought')

        player2.set_type('human', opposite=True)
        player2.set_team('cross')

        self.set_ai()

        rounds = try_int_input('How many rounds would you like to play?:', legal_range=range(1,10))

        round=1

        while round<=rounds:

            if rounds == round:

                print('=== Final Round Begins !! ===')

            else:

                print('=== Round {} Begins !! ==='.format(round))

            self.run_a_round(player1, player2)

            if rounds == round:

                print('=== End of Final Round !! ===')

            else:
                
                print('=== End of Round {} !! ==='.format(round))

            if rounds == round:
                print('The final scores are :')

            else:
                print('The current scores are :')

            print('player1 ({0}) has {1} points'.format(player1.kind, player1.score))
            print('player2 ({0}) has {1} points'.format(player2.kind, player2.score))


            round = round + 1

        if player1.score>player2.score:
            print('Player 1 Wins !')

        
        elif player2.score>player1.score:
            print('Player 2 Wins !')

        else:
            print("it's a Draw !")

        print('Thanks for playing :)')

    def run_a_round(self, first_player, second_player):

        self.game_board = board.board()

        result=None

        player_ind = 0

        player_list=[first_player, second_player]

        while result is None:

            #player1
            result = self.take_turn(player_list[player_ind], player_list[(player_ind+1) % 2])

            if result == True:

                player_list[player_ind].score_a_point()
            
            player_ind = (player_ind+1) % 2




        





