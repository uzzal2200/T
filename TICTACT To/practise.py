def display(board):
    print(f"\n|{board[0]} | {board[1]} | {board [2]}")
    print("--+--+--")
    print(f"|{board[3]} | {board[4]} | {board [5]}")
    print("--+--+--")
    print(f"|{board[6]} | {board[7]} | {board [8]}\n")


def winner(board, p):
    win = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7), (2,5,8),
        (0,4,8),(2,4,6)
        ]
    return any(board[a] == board[b] == board[c] == p for a,b,c in win)


def move(board, p):
    while True:
        m = int(input(f"player {p}, choose (1-9):  ")) - 1

        if board[m] == " ":
            board[m] = p
            break
        print("spot taken, try again ")


def draw(board):
    return " " not in board


def play():
    board, player = [" "]*9, "X"
    while True:

        display(board)
        move(board, player)
        if winner(board, player):
            display(board)
            break

        if draw(board):
            display(board)
            print("game is a draw")
            break
        player = "L" if player == "X" else "X"

play()

