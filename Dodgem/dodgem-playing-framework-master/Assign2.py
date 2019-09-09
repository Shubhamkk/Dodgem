#!/usr/bin/env python
'''
    File name: Assign2.py
    Author: Siddhant Kumar
    Email: saytosid@gmail.com
    Date created: 1 Oct 2017
    Date last modified: 1 Oct 2017
    Python Version: 3.0
'''

from framework import Board,Game,Player
import numpy as np
from MyPlayer import MyPlayer
from OtherPlayer import OtherPlayer
np.set_printoptions(suppress=True)

def run_game(player_1,player_2,max_num_moves,board_size=5):
    board = Board(size=board_size)
    game = Game(board,player_1,player_2)
    moves = 0
    while (moves < max_num_moves):
        moves += 1
        if game.step()==1:
            print ("Game Over, {} Lost".format(game.loser))
            return "Loser: {}".format(game.loser)
        board_matrix,turn = board.get_board_config()
        print(board_matrix)
        print(" ")




if __name__=='__main__':
    player_1 = OtherPlayer() # Random player
    player_2 = MyPlayer() # MyPlayer
    return_str = run_game(player_1,player_2,50)
    print ("Script returned: '{}'".format(return_str))

