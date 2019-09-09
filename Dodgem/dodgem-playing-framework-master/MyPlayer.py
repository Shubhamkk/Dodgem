from Player import Player

import operator
from Board import Board
import sys
class MyPlayer(Player):

	def __init__(self):
		self.count=0

	def get_move(self,board):

		moves = board.get_valid_moves()
		mn=Minimax()
		index=mn.minimax(board)
		
		return moves[index]
		
		
from copy import deepcopy

sys.setrecursionlimit(2000)
class Minimax(object):
	def __init__(self):
		
		self.ch=0
		self.count=0
		self.turn=2
		
	def minimax(self, board):
		"""Initiates a minimax search on the current game state."""
		
		values = map(lambda move: (move, self.mmax(self.next_state(board, move))),board.get_valid_moves())
		   # key=lambda x: x[1])
		index,value=max(enumerate([val[1] for val in values]),key=operator.itemgetter(1))
		#print([val[1] for val in values])
		#print(' ')
		#print(value,index)
		#print(self.count)
		return index

	def mmax(self, board):
		"""
		Maximizes the score against all of the next positions available
		for a specified game state.
		"""
		#print('mmax funtion')
		self.count+=1
		if self.ch==1 or self.count>=6:
			self.ch=0
			
			self.count-=1
			return self.evaluate(board)
		else:
			m1=max(map(lambda move: self.mmax(self.next_state(board, move)),board.get_valid_moves()))
		
		self.count-=1
		
		return m1

	def evaluate(self, board):
		"""Evaluates the state of a position for the configured player."""
		#print('evaluate function')


		if self.turn==2:
			return -1
		elif self.turn==1:
			return 1
		else:
			return 0
	def next_state(self, board, move):
		
		
		clone = deepcopy(board)
		x3,x2=self.make_move(move,clone)
		#clone.alternate_turn()
		if(x3=='lost'):
			self.ch=1
		self.turn=x2
		return clone
	def make_move(self,(piece,new_pos,extra_info),clone):
		
		
		if clone.turn == 1:
			#print('hello')
			for p in clone.player_1_pieces:
				if p.pos==piece.pos and p.color==piece.color and p.dead==piece.dead:
					p.pos = new_pos
					if extra_info==True:
						p.dead = True
					pieces_left = [item for item in clone.player_1_pieces if item.dead == False]
					if len(pieces_left)==0:
						return ('lost',2)
			clone.turn = 2

		elif clone.turn == 2:

			
			for p in clone.player_2_pieces:
				
				if p.pos==piece.pos and p.color==piece.color and p.dead==piece.dead:
					#print('hell')
					p.pos = new_pos
					if extra_info==True:
						p.dead = True
					pieces_left = [item for item in clone.player_2_pieces if item.dead == False]
					if len(pieces_left)==0:
						return ('lost',1)
					break	
			clone.turn = 1



		if len(clone.get_valid_moves()) == 0:
			# Other oppoment is blocked by this move
			#print('Blocked other player, You Lose')
			if clone.turn == 1:
				return ('lost', 2)
			elif clone.turn == 2:
				return ('lost', 1)

		# If normal play continues
		return ('game continues', None)
