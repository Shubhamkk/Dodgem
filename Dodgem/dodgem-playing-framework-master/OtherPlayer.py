
from framework import Player

class OtherPlayer(Player):

    def __init__(self):
        pass

    def get_move(self,board):
        '''
        :param board: Board object
        :return: (piece,new_position,BoardLeavingMove)
        '''
        moves = board.get_valid_moves()
        return moves[len(moves)-1]
