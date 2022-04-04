""" a class to hold the 3 x 3 grid
plan-
    method to show the current status
    method to update with a given move
    method to report the legal moves
    method to check if the game has ended

"""

from io import RawIOBase
from  helpers import linebreak , markers, buffer

class board():

    def __init__(self):
        """ init creates the board
        always size 3x3
        might be intersting to make this configurable
        """
        self.rows=3
        self.columns=3
        self.empty_box='_'

        # could us a numoy array
        # or a ditionary
        # start by trying simply nested lists
        self.grid = [[self.empty_box for i in range(self.columns)] for j in range(self.rows)]
        
    def show(self):
        """ show the current board state
        """
        print(linebreak)

        for i in range(self.rows):

            print(buffer + '|'.join(self.grid[i]))
            
        print(linebreak)

    def get_grid_value(self, location):

        assert self.check_within_board(location)

        return self.grid[location[0]][location[1]]

    def set_grid_value(self, location, marker):

        # only adds markers, doens't reset the board

        assert self.check_within_board(location)

        self.grid[location[0]][ location[1]] = marker

    def check_within_board(self, location):

        assert type(location) is list, 'location must be a list, got {0}: {1}'.format(type(location), location)


        if 0 <= location[0] <self.rows and 0 <= location[1] <self.columns:

            return True
        
        else:
             return False

    def check_legal_move(self, location):
        """ a move is only legal if it is the empty box and within the grid
        """
        if self.check_within_board(location) and (self.get_grid_value(location) == self.empty_box):

            return True

        else:

            return False
    
    def find_legal_moves(self):

        legal_moves=[]

        for i in range(self.rows):
            for j in range(self.columns):
                location=[i,j]
                if self.check_legal_move(location):
                    legal_moves.append(location)
        
        return legal_moves

    def check_for_victory(self):

        # must be three in a row, of either marker type
        # this is where a different data strucutre for the grid may be better

        # all values in "row" are the same:
        winner = None

        to_check=list()

        for i in range(3):

            to_check = to_check + [[[i,j] for j in range(3)]]

        for j in range(3):

            to_check = to_check + [[[i,j] for i in range(3)]]

        to_check = to_check + [[[i,i] for i in range(3)]]

        to_check = to_check + [[[i,2-i] for i in range(3)]]

        grid_values = [[self.get_grid_value(location) for location in tripple] for tripple in to_check]

        if True in [not False in [markers['cross'] == value  for value in tripple] for tripple in grid_values]:
            # 'X' has won
            return True

        elif True in [not False in [markers['nought'] == value  for value in tripple] for tripple in grid_values]:
            # '0' has won
            return True

        else:
            return False

    def check_for_full_board(self):

        if len(self.find_legal_moves()) ==0:

            return True
        
        else:
            False


    def copy_grid_to_other(self, other):
        """copy_grid_to_other

        copies the values in this board's grid to another board

        can't just set one grid equal to the other as they would alwasy have the same grid 
        """

        assert other.rows == self.rows

        assert other.columns == self.columns

        for i in range(self.rows):
            for j in range(self.columns):
                other.set_grid_value([i,j], self.get_grid_value([i,j]))
    



