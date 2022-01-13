"""
Authos: Miguel Condori
in the spaces of a grid of nine squares.
Tic-Tac-Toe is played according to the following rules.
The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a tie.
"""

def main ():

    restart = "y"

    while restart == "y":
        
        board = {'1': '1' , '2': '2' , '3': '3' ,
                 '4': '4' , '5': '5' , '6': '6' ,
                 '7': '7' , '8': '8' , '9': '9' }

        printBoard(board)

        game(board)

        # if player wants to restart the game or not.
        restart = input("Do ypu want to play again?(y/n) " )
        if restart.lower() == "n":  
            print("Good game. Thanks for playing!")


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game(board):

    turn = 'X'
    count = 0

    while count < 9:
        
        ask = turn + "'s turn to choose a square (1-9): "

        move = input(ask)

        # control if the place is empty
        if not board[move] in ("X","O"):
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.")
            continue

        exp1 = board['1'] == board['2'] == board['3']  # across the top
        exp2 = board['4'] == board['5'] == board['6']  # across the middle
        exp3 = board['7'] == board['8'] == board['9']  # across the bottom
        exp4 = board['1'] == board['4'] == board['7']  # down the left side
        exp5 = board['2'] == board['5'] == board['8']  # down the middle
        exp6 = board['3'] == board['6'] == board['9']  # down the right side
        exp7 = board['1'] == board['5'] == board['9']  # diagonal
        exp8 = board['7'] == board['5'] == board['3']  # diagonal

        # check if player X or O has won,after 5 moves. 
        if count >= 5:
            if exp1 or exp2 or exp3 or exp4 or exp5 or exp6 or exp7 or exp8:
                printBoard(board)
                print(" **** " +turn + " won. ****")                
                break

        # If neither X nor O wins and the board is full.
        if count == 9:
            print("It's a Tie!!")

        # change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        

# Call main to start this program.
if __name__ == "__main__":
    main()