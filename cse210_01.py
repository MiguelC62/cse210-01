"""
Authos: Miguel Condori
Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn
in the spaces of a grid of nine squares.
Tic-Tac-Toe is played according to the following rules.
The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a tie.
"""

def main ():
    
    board = {'1': '1' , '2': '2' , '3': '3' ,
             '4': '4' , '5': '5' , '6': '6' ,
             '7': '7' , '8': '8' , '9': '9' }

    board_keys = []

    restart = "y"

    while restart == "y":

        for key in board:
            board_keys.append(key)

        game(board, board_keys)

        # Now we will ask if player wants to restart the game or not.
        restart = input("Do want to play again?(y/n) " )
        if restart.lower() == "n":  
            print("Good game. Thanks for playing!")


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game(board, board_keys):

    turn = 'X'
    count = 0

    while count < 9:
        printBoard(board)
        ask = turn + "'s turn to choose a square (1-9): "

        move = input(ask)        

        if not board[move] in ("X","O"):
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if board['1'] == board['2'] == board['3'] != ' ': # across the top
                printBoard(board)
                print(" **** " +turn + " won. ****")                
                break
            elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
                printBoard(board)    
                print(" **** " +turn + " won. ****")
                break
            elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
                printBoard(board)
                print(" **** " +turn + " won. ****")
                break
            elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
                printBoard(board)
                print(" **** " +turn + " won. ****")
                break
            elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
                printBoard(board)
                print(" **** " +turn + " won. ****")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
                printBoard(board)
                print(" **** " +turn + " won. ****")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
                printBoard(board)
                print(" **** " +turn + " won. ****")
                break
            elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
                printBoard(board)
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
  


# Call main to start this program.
if __name__ == "__main__":
    main()