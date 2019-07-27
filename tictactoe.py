from IPython.display import clear_output
def displayBoard(b = [' ']*10):
    clear_output()
    print(b[7],'|',b[8],'|',b[9])
    print('_','|','_','|','_')
    print(b[4],'|',b[5],'|',b[6])
    print('_','|','_','|','_')
    print(b[1],'|',b[2],'|',b[3])

def playerInput():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Please choose player one\'s marker(O/X): ')
    return marker

def placeMarker(board,marker,position):
    board[position]=marker
    displayBoard(board)
    
def winCheck(board,marker):
    if len(set(board[1:4]))==1 and board[1]==marker:
        return True
    elif len(set(board[4:7]))==1 and board[4]==marker:
        return True
    elif len(set(board[7:10]))==1 and board[7]==marker:
        return True
    elif board[1]==board[4]==board[7]==marker:
        return True
    elif board[2]==board[5]==board[8]==marker:
        return True
    elif board[3]==board[6]==board[8]==marker:
        return True
    elif board[1]==board[5]==board[9]==marker:
        return True
    elif board[3]==board[5]==board[7]==marker:
        return True
    else:
        return Falsse
 
 def space_check(board,position):
    return board[position]==' '
    
 def fullBoard(board):
    return board.count(' ') < 1
 
 def player_choice(p):
    choice =0
    while not (1<=choice<=9):
            choice = int(input(f'Enter player {p}\'s move(1-9) :' ))
    return choice
 
 
 def playAgain():
    option = input('Do you want to play again(Y/N) ? ')
    return option=='Y' or option=='y'
    
print('Let\'s play TIC TAC TOE')
while True:
    if not playAgain():
        break
    player_1 = playerInput()
    if player_1=='X':
        player_2 = 'O'
    else:
        player_2='O'
    board=['#']+[' ']*9
    displayBoard(board) 
    choice=0
    while not fullBoard(board):
        #player one choice
        while not space_check(board,int(choice)):
            choice = player_choice('player one')
        placeMarker(board,player_1,int(choice))
        if winCheck(board,player_1):
            print('Player 1 wins')
            break
        #player two choice
        while not space_check(board,int(choice)):
            choice = player_choice('player two')
        placeMarker(board,player_2,int(choice))
        if winCheck(board,player_2):
            print('Player 2 wins')
            break
    else:
        print('Game Draw !!')
