""" want at least two ai

1) - implement the "random" ai as a class

2) - a smart ai that solves the games

they just need to know the current board state
 - who they are (their marker)

they need to be able to return a move when presented with this infomation

"""
import random

class CpuPlayer():

    def __init__(self, name):

        self.name=name


class RandomAI(CpuPlayer):

    def decide_move(self, board, marker):

        possible_moves = board.find_legal_moves()

        return random.choice(possible_moves)


class SlightlySmartAI(CpuPlayer):
    """look one move ahead
    make a winning move if possible (first one found if more than one)
    block a winning move for oppoent if possible (first one found if more than one)
    it can be the same method that is run to check for win / loss, just swap the marker tested
    otherise random
    """
    # will need to initialise it's own hypothetical game boards to test out the moves

    def test_move(self, move, board, marker):

        # put the move on a board (not the actual board)
        # need to be careful, the "grid" is stored in lists
        # need to create a new board, and copy the boardstate of the presented board
        # perhaps add a method to the board class to help here
        # debug this in interactive session like jupyter

        # is the game a win or a draw?

        # return result (win, draw, inconclusive) - the current player can't make a move that makes the opponent wim imediately
        # and the move that did it

        pass

    # test all legal moves for this turn , try to find a win

    # again, but now for opponent perpective, try to find a win, to block it

    # else choose randomly
    # the smarter ai should solve by looking deeper into future moves




class SolvedAI(CpuPlayer):
    """ could run a solver when initialised
    then just do a lookup when being used
    """



    def decide_move(self, board, marker):

        possible_moves = board.find_legal_moves()

        return random.choice(possible_moves)

    def assess_move():
        # try a move - what is the result
        # win - 2
        # draw = 1
        # loss = 0
        # game not ended - try another move (recursive)
        # return the result
        pass
