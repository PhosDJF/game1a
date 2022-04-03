""" use a class to make a player
"""
import helpers


class Player():

    def __init__(self):

        self.score=0   

    def set_type(self, kind, opposite=False):

        valid_types=['human', 'ai']

        assert kind in ['human', 'ai']

        if opposite:
            kind = [a for a in valid_types if not a == kind][0]

        self.kind = kind

    def set_team(self, team):
        
        assert team in ['nought', 'cross']

        self.team = team

        self.marker = helpers.markers[self.team]

    def score_a_point(self):

        self.score = self.score + 1

    def show_score(self):

        print('to do')


