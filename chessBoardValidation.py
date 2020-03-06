import pprint
colours = ['w', 'b']
piece_names = ['king', 'queen', 'pawn', 'rook', 'bishop', 'knight']

dict_to_count = {} #dict to count no of each piece
white_count = 0    #variable to keep count of white pieces
black_count = 0    #variable to keep count of black pieces

#Initializing the dict_to_count dictionary with all pieces value 0
for colour in colours:
    for piece_name in piece_names:
        piece = colour + piece_name #creates appropriate string like 'wking' or the like
        dict_to_count[piece] = 0

def isValidChessBoard(dict_chess):
    for position, piece_name in dict_chess.items():
        #Checking for valid position of the piece
        if int(position[0]) not in range(1, 9):
            return False
        if position[1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            return  False
        dict_to_count[piece_name] += 1 #Incrementing count of that piece if the position is valid


    #Declaring that the following variables refer to the global ones and not to be made local
    global white_count
    global black_count

    #Reading the input dictionary and increasing respective counts and also checking for valid count
    for piece, count in dict_to_count.items():
        if piece[0] == 'w':
            white_count += count
            #print(white_count)
        else:
            black_count += count
        if piece[1:] == 'pawn':
            if count not in range(0,9):
                return False
        if piece[1:] == 'king':
            if count != 1:
                return False
        if piece[1:] == 'queen':
            if count not in [0,1]:
                return False
        if piece[1:] == 'bishop':
            if count not in [0, 1, 2]:
                return False
        if piece[1:] == 'rook':
            if count not in [0, 1, 2]:
                return False
        if piece[1:] == 'knight':
            if count not in [0, 1, 2]:
                return False
    if white_count > 16 or black_count > 16:
        return False
    return True



chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3d': 'wking', '7d': 'bbishop'}

if(isValidChessBoard(chessBoard)):
    print("Valid Chessboard")
else:
    print("Invalid Chessboard")