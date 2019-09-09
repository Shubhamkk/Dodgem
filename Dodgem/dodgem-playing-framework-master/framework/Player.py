
import random

class Player:
    '''Defines a Random Move Player'''
    def __init__(self):
        pass

    def get_move(self,board):
        '''
        Override this method to create your player
        :param board: Board object
        :return: move i the format (piece,new_position,BoardLeavingMove)
        '''
        moves = board.get_valid_moves()
        return random.sample(moves, 1)[0]
