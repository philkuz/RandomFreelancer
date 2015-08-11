class Board:
	WHITE = 0
	BLACK = 1
	def __init__(self):
		# self.black = new Player(Player.BLACK)
		# self.white = new Player(Player.WHITE)
		self.resetBoard()
	def createBoard(self):
		#creates an empty board
		self.Board = [None]*8
		for i in range(0,8):
			self.Board[i] = [None]*8

		#since the Chess board is reflected across the center of hte board as the center of the acist, 
		# we can simply use the same code twice.


	def resetBoard(self):		
		if(not self.Board):
			self.createBoard()
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
				coord = [pieceCt*8, nPawnY]
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
			self.Board[coord[0], coord[1]] = piece
		else:
			self.Board[piece.position[0], piece.position[1]] = piece
	#getting a piece from a string of hte position in the format [a-h][1-8]
	def getPiece(self, pos):
		if isinstance(pos, basestring):
			pos = getCrdPos(pos)
		if pos:
			return self.Board[pos[0], pos[1]]
		else:
			return None
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



# class Player:
# 	BLACK = 1
# 	WHITE = 0
# 	#color should be an element of ("black", "white", 0, 1)
# 	def __init__(self, color):
# 		if(color == "black"):
# 			self.color = BLACK
# 		elif(color == "white"):
# 			self.color = WHITE
# 		else:
# 			self.color = color
# 		self.pieces = []
# 	def getType(self):
# 		color = ""
# 		if(self.color == WHITE):
# 			return "white"
# 		elif(self.color == BLACK):
# 			return "black"
# 		else:
# 			return None
# 	def resetPieces(self):


class Piece: 
	def __init__(self, color, pos):
		self.color=  color
		if(isinstance(pos, basestring)):
			self.position = getCrdPos(pos)
		else:
			self.position = pos
		self.Display = "Z"
	def getDisplay(self):
		return self.Display
	def getMoves(self, board):
		return []
class Pawn(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "P"
	def getMoves(self, board):
		#generate possible moves

		#eliminate moves that aren't legal

class Knight(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "N"
class Queen(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "Q"
class King(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "K"
class Rook(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "R"
class Bishop(Piece):
	def __init__(self, color, pos):
		Piece.__init__(self, color, pos)
		self.Display = "B"
