""" want at least two ai

1) - implement the "random" ai as a class

2) - a smart ai that solves the games

they just need to know the current board state
 - who they are (their marker)

they need to be able to return a move when presented with this infomation

"""
import random
import board

class CpuPlayer():

    def __init__(self, name):

        self.name=name


class RandomAI(CpuPlayer):

    def decide_move(self, board, player, opponent):

        possible_moves = board.find_legal_moves()

        return random.choice(possible_moves)


class SlightlySmartAI(CpuPlayer):
    """look one move ahead
    make a winning move if possible (first one found if more than one)
    block a winning move for oppoent if possible (first one found if more than one)
    it can be the same method that is run to check for win / loss, just swap the marker tested
    otherise random
    """

    def decide_move(self, board, player, opponent):

        move, _ = find_move(board, player, opponent)
        return move


class SolvedAI(CpuPlayer):
    """ could run a solver when initialised
    then just do a lookup when being used
    """

    def decide_move(self, board, player, opponent):

        
        move, _ = find_move(board, player, opponent, reccursive=True)

        print('The AI is doing the move: {}'.format(move))
        return move

def test_move(move, current_board, marker):
    """test_move
    
    what if we do the move, what happens?
    2 - you win
    1 - you draw
    0 - no result
    
    """

    # put the move on a board (not the actual board)
    # need to be careful, the "grid" is stored in lists
    # need to create a new board, and copy the boardstate of the presented board
    local_board = board.board()
    
    current_board.copy_grid_to_other(local_board)
    
    local_board.set_grid_value(move,marker)

    # is the game a win or a draw?
    if local_board.check_for_victory() == True:
        
        result = 2
        
    elif local_board.check_for_full_board() == True:
        
        result = 1
        
    else:
        
        result = 0
    
    return result

def find_move(current_board, player, opponent, reccursive=False):
        
    possible_moves = current_board.find_legal_moves()

    results = list()

    # test all legal moves for this turn , try to find a win
    for move in possible_moves:

        results.append(test_move(move, current_board, player.marker))

    if 2 in results:

        return possible_moves[results.index(2)], 2

    elif 1 in results:

        return possible_moves[results.index(1)], 1
 
    # again, but now for opponent perpective, try to find a win, to block it
    else:

        results = list()

        for move in possible_moves:

            results.append(test_move(move, current_board, opponent.marker))

        if 2 in results:

                return possible_moves[results.index(2)], 0 # don't want opponent to win

        elif 1 in results:

            return possible_moves[results.index(1)], 1

        # else choose randomly
        # the smarter ai should solve by looking deeper into future moves       
        elif reccursive:
            
            #create test boards:
            results2=list()

            for move in possible_moves:



                new_board = board.board()

                current_board.copy_grid_to_other(new_board)

                new_board.set_grid_value(move,player.marker)

                #_ = input('new_board is : ')
                #new_board.show()

                #find next move - from opponents perspective
                move, score = find_move(new_board, opponent, player, reccursive=True)

                results2.append(score)

            if 2 in results2:

                return possible_moves[results2.index(2)], 2

            elif 1 in results2:

                return possible_moves[results2.index(1)], 1

            else:

                return possible_moves[0], 0 # will avoid selecting this from the results 
 
        # not running recursion, make random choice
        else:
            
            return random.choice(possible_moves), 0