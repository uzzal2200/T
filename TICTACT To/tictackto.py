# # Tic-Tac-Toe Game (Short Version with Comments)

# # Function to display the current state of the board
# def display(board):
#     # Show 3 rows of the board in a nice format
#     print(f"\n{board[0]} | {board[1]} | {board[2]}")
#     print("--+---+--")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print("--+---+--")
#     print(f"{board[6]} | {board[7]} | {board[8]}\n")

# # Function to check if a player has won
# def winner(board, p):
#     # All possible winning combinations (rows, columns, diagonals)
#     wins = [
#         (0,1,2), (3,4,5), (6,7,8),  # Horizontal lines
#         (0,3,6), (1,4,7), (2,5,8),  # Vertical lines
#         (0,4,8), (2,4,6)            # Diagonals
#     ]
#     # Return True if any winning pattern is filled with the player's symbol
#     return any(board[a] == board[b] == board[c] == p for a, b, c in wins)

# # Function to check if the game is a draw
# def draw(board):
#     # Draw occurs if there are no empty spaces left
#     return " " not in board

# # Function to handle a player's move
# def move(board, p):
#     while True:
#         try:
#             # Ask the player to choose a position (1-9)
#             m = int(input(f"Player {p}, choose (1-9): ")) - 1
#             # Place symbol if spot is empty
#             if board[m] == " ":
#                 board[m] = p
#                 break
#             print("Spot taken. Try again.")
#         except (ValueError, IndexError):
#             # Handle wrong inputs (non-numbers or out of range)
#             print("Invalid choice! Pick 1-9.")

# # Main function to control the game flow
# def play():
#     # Create an empty board and set the first player to X
#     board, player = [" "] * 9, "X"
#     while True:
#         display(board)  # Show the board
#         move(board, player)  # Get player's move
#         # Check if the player has won
#         if winner(board, player):
#             display(board)
#             print(f"🎉 Player {player} wins!")
#             break
#         # Check if the game is a draw
#         if draw(board):
#             display(board)
#             print("🤝 It's a draw!")
#             break
#         # Switch to the other player
#         player = "O" if player == "X" else "X"

# # Start the game
# play()











def display(board):
    print(f"\n|{board[0]} | {board[1]} | {board[2]}|")
    print("---+---+---")
    print(f"|{board[3]} | {board[4]} | {board[5]}|")
    print("---+---+---")
    print(f"|{board[6]} | {board[7]} | {board[8]}|\n")


# display(['X', 'O', 'X', ' ', 'O', ' ', ' ', 'X', 'O'])

def winner(board, p):
    wins  = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7), (2,5,8),
        (0,4,8),(2,4,6)
    ]

    return any(board[a] == board[b] == board[c] == p for  a,b,c in wins)


def draw(board):
    return " " not in board


def move(board, p):
    while True:
        m = int(input(f"player {p}, choose (1-9):  ")) - 1

        if board[m] == " ":
            board[m] = p
            break
        print("spot taken, try again ")

def play():
    board, player  = [" "]*9, "X"
    while True:
        display(board)
        move(board,player)
        if winner(board, player):
            display(board)
            print(f" player {player} wins the game")
            break

        if draw(board):
            display(board)
            print("It is a draw game")
            break

        player = "L" if player == "X" else "X"

play()



