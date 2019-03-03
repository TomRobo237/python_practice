theBoard = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
            'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
            'LOW-L': ' ', 'LOW-M': ' ', 'LOW-R': ' '}
def printBoard(board):
    print(board['TOP-L'] + '|' + board['TOP-M'] + '|' + board['TOP-R'])
    print('-+-+-')
    print(board['MID-L'] + '|' + board['MID-M'] + '|' + board['MID-R'])
    print('-+-+-')
    print(board['LOW-L'] + '|' + board['LOW-M'] + '|' + board['LOW-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print( turn + '\'s turn\nWhere will you place?')
    move = input()
    if move.upper() not in theBoard.keys():
        print('Not on the board!\ntry top/mid/low-L/M/R')
    else:
        theBoard[move.upper()] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
            

