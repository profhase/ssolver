import sys
from entities import *

class Field():

	def __init__(self, val):
		self.options = set(list(range(1,10)))
		self.val = val

	def __str__(self):
		return self.val


class Board():

	def __init__(self, fname):
		self._board = []
		self.read_file(fname)
		self.rows = []
		self.columns = []
		self.squares = []

	def read_file(self, fname):
		'''Reads a sudoku file with spaces
		or zeros as empty fields'''
		with open(fname,'r') as puzzle:
			for line in puzzle:
				try:
					conv = map(int,list(line.replace(' ',0)))
				except ValueError as e:
					sys.stderr.write("Invalid values in Puzzle")
					sys.exit(1)
					
				self._board.append([Field(c) for c in conv])

	def create_rows(self):
		for row in self._board:
			self.rows.append(Line(row))

	def create_columns(self):
		for i in range(9):
			col = self._board[i][j]
					
