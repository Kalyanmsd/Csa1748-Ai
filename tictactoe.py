# Tic-Tac-Toe Game in Python
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True
def make_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("The spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is X, Player 2 is O")
    print("Enter numbers from 1 to 9 to place your mark on the board as shown below:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n")
    current_player = "X"  
    while True:
        print_board(board)
        make_move(board, current_player)
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"
tic_tac_toe()
