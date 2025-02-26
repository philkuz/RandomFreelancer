
class Board:
	WHITE = 0
	BLACK = 1
	def __init__(self):
		# self.black = new Player(Player.BLACK)
		# self.white = new Player(Player.WHITE)
		self.board = None
		self.createBoard()
	def createBoard(self):
		#creates an empty board
		self.board = [None]*8
		for i in range(0,8):
			self.board[i] = [None]*8

	def resetBoard(self):		
		# if(not self.board):
		self.createBoard()
		#since the Chess board is reflected across the center of hte board as the center of the acist, 
		# we can simply use the same code twice.
		for color in range(0,2):
			pawnY = 1+color*5
			nPawnY = color*7
		#generate pawns first
			for pawnCt in range(0,8):
				coord = [pawnCt, pawnY]
				curPawn = Pawn(color, coord)
				self.setPiece(curPawn)
			
			#lumps three generations based on the line of symmetry that divides all except queen and king
			for pieceCt in range(0,2):
			#rooks
				coord = [pieceCt*7, nPawnY]
				curRook = Rook(color, coord)
				self.setPiece(curRook)
			#knights
				coord = [1+pieceCt*5, nPawnY]
				curKnight = Knight(color, coord)
				self.setPiece(curKnight)
			#bishops
				coord = [2+pieceCt*3, nPawnY]
				curBishop = Bishop(color,coord)
				self.setPiece(curBishop)
		#queen
			coord = [3, nPawnY]
			curQueen = Queen(color, coord)
			self.setPiece(curQueen)
		#king
			coord = [4, nPawnY]
			curKing = King(color, coord)
			self.setPiece(curKing)
	
	def setPiece(self, piece, coord = None):
		if(not coord):
			if(not piece):
				print "Error, None piece entered w/o coordinates"
			else:
				self.board[piece.position[0]][ piece.position[1]] = piece
		else:
			self.board[coord[0], coord[1]] = piece
	#getting a piece from a string of hte position in the format [a-h][1-8]
	def getPiece(self, pos):
		if isinstance(pos, basestring):
			pos = getCrdPos(pos)
		if pos:
			return self.board[pos[0]][pos[1]]
		else:
			return None
	def printBoard(self):
		outputStr = ""
		outputStr = "    a   b   c   d   e   f   g   h\n"
		
		for i in range(0,8):
			outputStr += " " + str(i + 1) + " "
			# outputStr+= " " +chr(ord('a')+i) + " "
			for j in range(0,8):
				piece = self.getPiece([j, i])
				if not piece:
					outputStr += " xx ";
				else:
					outputStr += " " + piece.getDisplay() + " ";
			outputStr +="\n"
		return outputStr
	def legalPosition(self, pos, piece=None):
		if(not legalPosition(pos)):
			return False
		#if no piece is selected, that means that the position is on the board which is all that matters
		if(piece == None):
			return True
		#otherwise should check if the Piece on the position is the same color or not
		else:
			curPiece = self.getPiece(pos)
			if(curPiece):
				if curPiece.color == piece.color:
					return False
			# WARNING: DOES NOT CHECK IF THE KING WILL BE IN CHECK AFTER MOVE. A "LEGAL POSITION" IN THIS CONTEXT DOES NOT MEAN THAT A MOVE
			# WILL STOP A CHECK OR A MOVE DOES NOT PUT THE CURRENT PLAYER INTO CHECK
			return True
	#get the string position of the coordinate
	@staticmethod
	def getStrPos(crdPos):
		if(len(crdPos) != 2):
			print "Improper length format"
			return None
		pos = [chr(crdPos[0]+ord('a')), str(crdPos[1]+1)]
		return ''.join(pos)
	#get the coordinate position of the string (ie "a4" -> [0,3])
	@staticmethod
	def getCrdPos(strPos):
		if(len(strPos) != 2):
			print "Error in conversion of " + strPos + "to a coordinate"
			return None
		pos = [strPos[0], strPos[1]]
		outputPos = [ord(pos[0])-ord('a'), int(pos[1])-1]
		return outputPos
	@staticmethod
	def legalPosition(pos):
		crd = []
		if(isinstance(pos, basestring)):
			crd = getCrdPos(pos)
		else:
			crd = pos
		for com in crd:
			if (com > 7 or com < 0):
				return False
		return True
	

class Piece: 
	def __init__(self, color, pos):
		self.color=  color
		if(isinstance(pos, basestring)):
			self.position = getCrdPos(pos)
		else:
			self.position = pos
		self.Display = "Z"
		self.Name ="General Piece"
	def getDisplay(self):
		if self.color == 0:
			return "w"+self.Display
		else:
			return "b"+self.Display
		
	def checkMoves(self, moves, board):
		legalMoves = []
		for move in moves:
			absMove = [pos[0]+move[0], pos[1]+move[1]]
			if(board.legalPosition(absMove, self)):
				legalMoves.append(absMove)
		return legalMoves

	def getMoves(self, board):
		return []
class Pawn(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "P"
		self.Name = "pawn"
	#board should be of type Board
	def getMoves(self, board):

		# set the direction of the move: f(white, black) => (1,-1)
		direction = (-1)**self.color
		moves = [[-1, direction], [0, direction], [1, direction]]
		legalMoves = self.checkMoves(moves, board)
		return legalMoves	


class Knight(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "N"
		self.Name = "knight"
	# def getMoves(self, board)

class Queen(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "Q"
		self.Name = "queen"
class King(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "K"
		self.Name = "king"
class Rook(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "R"
		self.Name = "rook"
class Bishop(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "B"
		self.Name = "bishop"
bd = Board()
bd.resetBoard()
s = bd.printBoard()
print s
