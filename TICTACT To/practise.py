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



def draw(board):
    # সব ঘর পূর্ণ হলেও ড্র হবে না, বরং র‍্যান্ডমভাবে একটি ঘর খালি করে দেবে
    if " " not in board:
        import random
        idx = random.randint(0, 8)
        board[idx] = " "
        print(f"Randomly cell {idx+1} খালি করা হলো!")
        return False  # ড্র হবে না
    return False  # ড্র না হলে False


def move(board, p):
    while True:
        m = int(input(f"player {p}, choose (1-9):  ")) - 1
        if board[m] == " ":
            board[m] = p
            break;
        print(" try again ")


def play():
    board , player = [" "]*9, "X"
    while True:
        display(board)
        move(board, player)
        if winner(board,player):
            display(board)
            print(f" player {player} wins the game")
            break

        if draw(board):
            display(board)
            print(" game is draw")
            break


        player = "O" if player == "X" else "X"

play()




def draw(board):
    # সব ঘর পূর্ণ হলেও ড্র হবে না, বরং র‍্যান্ডমভাবে একটি ঘর খালি করে দেবে
    if " " not in board:
        import random
        idx = random.randint(0, 8)
        board[idx] = " "
        print(f"Randomly cell {idx+1} খালি করা হলো!")
        return False  # ড্র হবে না
    return False  # ড্র না হলে False

# ...existing code...