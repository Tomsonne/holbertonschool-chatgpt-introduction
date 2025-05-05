#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Row and column must be 0, 1, or 2. Try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
