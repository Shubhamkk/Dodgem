
class Piece:
    def __init__(self,color='black',position=(-1,-1)):
        '''
        :param color: color of the piece, by default black
        :param position: position of piece
        '''

        self.color = color
        self.pos = position
        self.dead = False
