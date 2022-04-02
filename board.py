""" a class to hold the 3 x 3 grid
plan-
    method to show the current status
    method to update with a given move
    method to report the legal moves
    method to check if the game has ended

"""

from  helpers import linebreak 

class board():

    def __init__(self):
        """ init creates the board
        always size 3x3
        might be intersting to make this configurable
        """
        self.rows=3
        self.columns=3
        self.empty_box='_'

        # a player could be a class
        self.players = ['nought', 'cross']

        self.markers = {'nought':'0', 'cross':'X'}

        # could us a numoy array
        # or a ditionary
        # start by trying simply nested lists
        self.grid = [[self.empty_box for i in range(self.columns)] for j in range(self.rows)]
        
    def show(self):
        """ show the current board state
        """
        print(linebreak)

        # TODO add a buffer so the board is more central when printed
        for i in range(self.rows):
            print('|'.join(self.grid[i]))
        print(linebreak)

    def get_grid_value(self, location):

        assert self.check_within_board(location)

        return self.grid[location[0]][location[1]]

    def set_grid_value(self, location, player):

        # only adds markers, doens't reset the board

        assert self.check_within_board(location)

        self.grid[location[0]][ location[1]] = self.markers[player]

    def check_within_board(self, location):

        if 0 <= location[0] <=self.rows and 0 <= location[1] <=self.columns:

            return True
        
        else:
             return False

    def check_legal_move(self, location):
        """ a move is only legal if it is the empty box
        """
        assert self.check_within_board()

        if self.get_grid_value(location) == self.empty_box:

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

    



