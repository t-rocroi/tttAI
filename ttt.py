# python 3

score = 0

def Clear():
	import os
	os.system('cls' if os.name == 'nt' else 'clear')

class Board():
	def __init__(self, rows=3, columns=3):
		self.rows = rows
		self.columns = columns
		self.board = {0:['O', 'X', ' '],
					  1:['X', 'X', 'O'],
					  2:[' ', 'O', ' ']}

	def ResetBoard(self):
		for i in range(self.rows):
			row = []
			for j in range(self.columns):
				row.append(' ')
			self.board[i] = row

	def DisplayBoard(self):
		# Clear()
		for row in self.board.values():
			print('| ', end='')
			for element in row:
				print(element, end = ' | ')
			print('')

	def CheckSquare(self, row, col):
		if self.board[row][col] == 'X':
			return 'X'
		elif self.board[row][col] == 'O':
			return 'O'
		else:
			return ' '

	def AddPiece(self, row, col, token):
		if self.CheckSquare(row, col) != ' ':
			print('Error, cannot play in this square, try again')
			return -1
		else:
			self.board[row][col] = token
			print('Added {} at ({}, {})'.format(token, row, col))
			self.DisplayBoard()
			return 1

class Move():
	def __init__(self):
		self.row = -1
		self.col = -1

class TTTAI():  # how to set which player it plays for?
	def __init__(self, p1token, p2token):
		self.p1token = p1token
		self.p2token = p2token
		self.current = p2token

	def IsMovesLeft(self, board):
		for i in range(board.rows):
			for j in range(board.columns):
				if board.board[i][j] == ' ':
					return True
		return False

	def CellEmpty(self, board, row, col):
		if board.board[row][col] == ' ':
			return True
		else:
			return False

	def Evaluate(self, board, p1token, p2token):
		if self.CheckHoriz(board, p1token, p2token):
			return self.CheckHoriz(board, p1token, p2token)
		elif self.CheckVerti(board, p1token, p2token):
			return self.CheckVerti(board, p1token, p2token)
		elif self.CheckDiags(board, p1token, p2token):
			return self.CheckDiags(board, p1token, p2token)
		else:
			return 0
		
	def CheckHoriz(self, board, p1token, p2token):
		for i in range(board.rows):
			if board.board[i][0] == board.board[i][1] == board.board[i][2]:
				if board.board[i][0] == p1token:
					return 10
				elif board.board[i][0] == p2token:
					return -10

	def CheckVerti(self, board, p1token, p2token):
		for i in range(board.columns):
			if board.board[0][i] == board.board[1][i] == board.board[2][i]:
				if board.board[0][i] == p1token:
					return 10
				elif board.board[0][i] == p2token:
					return -10

	def CheckDiags(self, board, p1token, p2token):
		if board.board[0][0] == board.board[1][1] == board.board[2][2]:
			if board.board[0][0] == p1token:
				return 10
			elif board.board[0][0] == p2token:
				return -10
		elif board.board[0][2] == board.board[1][1] == board.board[2][0]:
			if board.board[0][2] == p1token:
				return 10
			elif board.board[0][2] == p2token:
				return -10

	def MinMax(self, board, depth, IsMax):
		# board.DisplayBoard()
		score = self.Evaluate(board, self.p1token, self.p2token)
		# print("Evaluate produced: ", score, '\n')
		# print('current depth: ', depth)
		if score == 10:  # maximizer won
			return score
		elif score == -10:  # minimizer won
			return score
		elif self.IsMovesLeft(board) == False:
			return 0

		# if depth > 3:
		# 	return score

		## control flow between Maximizer and Minimizer turns
		if IsMax: # True, eg maximizer's move
			best = -100
			for i in range(board.rows):
				for j in range(board.columns):
					if self.CellEmpty(board, i, j):
						board.board[i][j] = self.p1token  # temporarily make the move
						best = max(best, self.MinMax(board, depth+1, not IsMax))-depth
						# print("Maximizer best: ", best)
						board.board[i][j] = ' '  # undo the move
			return best
		else:  # False, eg minimizer's move
			best = 100
			for i in range(board.rows):
				for j in range(board.columns):
					if self.CellEmpty(board, i, j):
						board.board[i][j] = self.p2token  # temporarily make the move
						best = min(best, self.MinMax(board, depth+1, not IsMax))+depth 
						# print("Minimizer best: ", best)
						board.board[i][j] = ' '  # undo the move
			return best

	def MinMaxAB(self, board, depth, node, IsMax, alpha, beta):
		score = self.Evaluate(board)
		# board.DisplayBoard()
		# print("Evaluate produced: ", score, '\n')
		# print('current depth: ', depth)
		if score == 10:  # maximizer won
			return score
		if score == -10:  # minimizer won
			return score
		if self.IsMovesLeft(board) == False:
			return 0

		## control flow between Maximizer and Minimizer turns
		if IsMax: # True, eg maximizer's move
			best = -100
			for i in range(board.rows):
				for j in range(board.columns):
					if self.CellEmpty(board, i, j):
						board.board[i][j] = player  # temporarily make the move
						## MinMaxAB(self, board, depth, node, IsMax, alpha, beta):
						best = max(best, self.MinMaxAB(board, depth+1, 0, not IsMax, alpha, beta)) - depth
						print('Maximizer best: ', best)
						board.board[i][j] = ' '  # undo the move
			return best
		else:  # False, eg minimizer's move
			best = 100
			for i in range(board.rows):
				for j in range(board.columns):
					if self.CellEmpty(board, i, j):
						board.board[i][j] = opponent  # temporarily make the move
						## MinMaxAB(self, board, depth, node, IsMax, alpha, beta):
						best = min(best, self.MinMaxAB(board, depth+1, 0, not IsMax, alpha, beta)) + depth
						print('Minimizer best: ', best)
						board.board[i][j] = ' '  # undo the move
			return best

	def FindBestMove(self, board, token):
		self.current = token
		BestMove = Move()
		if token == self.p1token:
			BestValue = -100
			IsMax = False
			for i in range(board.rows):
				for j in range(board.columns):
					# print('Cell: ', i, j, 'value: ', board.board[i][j])
					if self.CellEmpty(board, i, j):
						board.board[i][j] = token
						print('Cell:  {} {} is empty, trying '.format(i, j), board.board[i][j])
						MoveValue = self.MinMax(board, 0, IsMax)
						# MoveValue = self.MinMaxAB(board, 0, 0, False, -1000, 1000)
						## MinMaxAB(self, board, depth, node, IsMax, alpha, beta):
						# print("With this move, updated board is:", MoveValue, '\n')
						board.board[i][j] = ' '
						if MoveValue > BestValue:  # note the '>' symbol
							BestMove.row = i
							BestMove.col = j
							BestValue = MoveValue
			# print("The value of the best move is {}".format(BestValue))
		elif token == self.p2token:
			BestValue = 100
			IsMax = True
			for i in range(board.rows):
				for j in range(board.columns):
					# print('Cell: ', i, j, 'value: ', board.board[i][j])
					if self.CellEmpty(board, i, j):
						board.board[i][j] = token
						# print('Cell:  {} {} is empty, trying '.format(i, j), board.board[i][j])
						MoveValue = self.MinMax(board, 0, IsMax)
						# MoveValue = self.MinMaxAB(board, 0, 0, False, -1000, 1000)
						## MinMaxAB(self, board, depth, node, IsMax, alpha, beta):
						# print("With this move, updated board is:", MoveValue, '\n')
						board.board[i][j] = ' '
						if MoveValue < BestValue:  # note the '<' symbol
							BestMove.row = i
							BestMove.col = j
							BestValue = MoveValue
			# print("The value of the best move is {}".format(BestValue))
		return BestMove

player = 'X'
opponent = 'O'

## set up
gameboard = Board()
print('')
# print('The Current Board:')
# gameboard.DisplayBoard()
print('')
Finn = TTTAI(player, opponent)
## end setup

# BestMove = Finn.FindBestMove(gameboard, player)
# print('The best move is {}, {}'.format(BestMove.row, BestMove.col))
# gameboard.board[BestMove.row][BestMove.col] = Finn.current
# gameboard.DisplayBoard()
# print('')

def NewGame():
	gameboard.ResetBoard()
	print('The Current Board:')
	gameboard.DisplayBoard()

def disp():
	# Clear()
	gameboard.DisplayBoard()

def PlayMove(token, row, col):
	gameboard.board[row][col] = token
	disp()

def Player1():
	move = Move()
	choice = input('What is your move? ')
	move.row = int(choice.replace(' ','').split(',')[0])
	move.col = int(choice.replace(' ','').split(',')[1])
	PlayMove(player, move.row, move.col)

def Player2():
	BestMove = Finn.FindBestMove(gameboard, opponent)
	print('AI plays {}, {}'.format(BestMove.row, BestMove.col))
	PlayMove(opponent, BestMove.row, BestMove.col)

NewGame()

while 1:
	print('')
	if Finn.IsMovesLeft(gameboard) == False:
		print("")
		print("Game over... stalemate")
		print("")
		break
	Player1()
	if Finn.IsMovesLeft(gameboard) == False:
		print("")
		print("Game over... stalemate")
		print("")
		break
	Player2()
	if Finn.IsMovesLeft(gameboard) == False:
		print("")
		print("Game over... stalemate")
		print("")
		break
	print("Current board value:", Finn.Evaluate(gameboard, player, opponent))
	if Finn.Evaluate(gameboard, player, opponent) == 10:
		print('')
		print("Congrats! You beat me")
		print('')
		break
	elif Finn.Evaluate(gameboard, player, opponent) == -10:
		print('')
		print("Dude, I beat you...")
		print('')
		break
