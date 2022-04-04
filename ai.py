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

    TODO - compare this ai to a lookup of each position, can it accurately paly them?

    """

    def decide_move(self, board, player, opponent):

        # the sign is 1 to start because we want to win
        move, result = find_move_recursive(board, player, opponent, 1)

        #print('solved ai thinks the result will be {}'.format(result))
        # TODO add one-liners to indicate the ai's confidence

        return move

def test_move(move, current_board, marker):
    """test_move
    
    what if we do the move, what happens?
    1 - you win
    0 - you draw
    None - no result
    
    """

    # put the move on a board (not the actual board)
    # need to be careful, the "grid" is stored in lists
    # need to create a new board, and copy the boardstate of the presented board
    local_board = board.board()
    
    current_board.copy_grid_to_other(local_board)
    
    local_board.set_grid_value(move,marker)

    # is the game a win or a draw?
    if local_board.check_for_victory() == True:
        
        result = 1
        
    elif local_board.check_for_full_board() == True:
        
        result = 0
        
    else:
        
        result = None
    
    return result

def find_move(current_board, player, opponent):
        
    possible_moves = current_board.find_legal_moves()

    results = list()

    

    # test all legal moves for this turn , try to find a win
    for move in possible_moves:
        
        

        results.append(test_move(move, current_board, player.marker))

    if 1 in results:

        return possible_moves[results.index(1)], 1

    elif 0 in results:

        return possible_moves[results.index(0)], 0
 
    # again, but now for opponent perpective, try to find a win, to block it
    else:

        results = list()

        for move in possible_moves:

            results.append(test_move(move, current_board, opponent.marker))

        if 1 in results:

                return possible_moves[results.index(1)], 0 

        elif 0 in results:

            return possible_moves[results.index(0)], 0

        # make random choice
        else:
            
            return random.choice(possible_moves), 0



def find_move_recursive(current_board, player, opponent, sign):
    """find_move_recursive

    try to find a move that wins

    else consider the opponeents options by calling this function recursively

    sign used to correct for who's perspecitve we are working with
        1 means player wants to win
        -1 means opponent wants to win

    the return should always be MOVE, RESULT
    where move is a list [a,b] and RESULT is an int, [-1, 0, 1]
    """
    assert sign in [-1, 1]    

    #print('solved ai is considering the board {}'.format(current_board.show()))

    possible_moves = current_board.find_legal_moves()

    results = [test_move(move, current_board, player.marker) for move in possible_moves]

    # one of the moves results in a win
    if 1 in results:

        return possible_moves[results.index(1)], 1*sign

    # only one legal move
    elif len(possible_moves) == 1:

        # it isn't a win, becasue we already checked for that
        # so return 0 for a draw
        return possible_moves[0], 0

    # there isn't an easy decision to make, so consider the options the opponent will will have

    else:
        
        opponents_results = list()

        for move in possible_moves:

            # create a new board and trial the results
            new_board = board.board()

            current_board.copy_grid_to_other(new_board)

            new_board.set_grid_value(move,player.marker)

            # swap the players around and the sign
            opponents_results.append(find_move_recursive(new_board, opponent, player, sign*-1))


        # opponents_results is a list like [ (move1, score1), (move2, score2)... ]
        # what to find the move that has the maximum score
        moves=[r[0] for r in opponents_results ]

        scores=[r[1] for r in opponents_results ]

        # when sign is 1 we want the min
        if sign==1:
            best_index = scores.index(min(scores))

        # when sign is -1 we want the min
        if sign==-1:
            best_index = scores.index(max(scores))

        return moves[best_index], scores[best_index]
