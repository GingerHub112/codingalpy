board = {
    '7': ' ', '8': ' ', '9':' ',
    '4': ' ', '5': ' ', '6':' ',
    '1': ' ', '2': ' ', '3':' '
}

boardKeys = []

for i in board:
    boardKeys.append(i)

def printBoard(board):
    print(board["7"], "|", board["8"], "|", board["9"])
    print("-+-+")
    print(board["4"], "|", board["5"], "|", board["6"])
    print("-+-+")
    print(board["1"], "|", board["2"], "|", board["3"])

def game():
    turn = 'X'
    count = 0
    for i in range(0, 10):
        
        printBoard(board)

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("This operation isn't permitted")
            continue
    
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':
                printBoard(board)
                print(turn, "won")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                printBoard(board)
                print(turn, "won")
                break
            elif board['1'] == board['2'] == board['3'] != ' ':
                printBoard(board)
                print(turn, "won")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                printBoard(board)
                print(turn, "won")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                printBoard(board)
                print(turn, "won")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                printBoard(board)
                print(turn, "won")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                printBoard(board)
                print(turn, "won")
                break
            elif board['7'] == board['5'] == board['3'] != ' ':
                printBoard(board)
                print(turn, "won")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print(turn, "won")
                break
        
        if count == 9:
            print("Tie!")

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart = input("Want to play again (Y/N) ")
    if restart=="y" or restart=="Y":
        for x in boardKeys:
            board[x] = " "

        game()

game()