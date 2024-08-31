import os
import random
import json

# Define a global dictionary to map move numbers to board coordinates
MOVE_MAP = {
    "1": (0, 0), "2": (0, 1), "3": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "7": (2, 0), "8": (2, 1), "9": (2, 2)
}

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_board():
    # Initialize the board with numbers 1 to 9 for player selection
    return [
        ["1", "2", "3"],  # Top row
        ["4", "5", "6"],  # Middle row
        ["7", "8", "9"]   # Bottom row
    ]

def print_board(board):
    # Print the board in a readable format
    clear_screen()  # Clear the screen for a fresh display
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

def check_winner(board):
    # Check for a winner in rows, columns, or diagonals
    for i in range(3):
        # Check for a winner in each row
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
    # Check for a winner in each column
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check for a winner in the two diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None  # Return None if there's no winner yet

def make_move(board, move, player):
    # Make a move on the board if the move is valid
    if move in MOVE_MAP:
        row, col = MOVE_MAP[move]
        # Check if the cell is empty
        if board[row][col] not in ["X", "O"]:
            board[row][col] = player
            return True
        else:
            print("Cell is already occupied.")
            return False
    else:
        print("Invalid move! Please enter a number between 1 and 9.")
        return False
def ai_move(board, current_player, filename='game_data.json'):
    # AI makes a move based on old data from a json file
    game_data = load_game_data(filename)

    # Get all available moves
    available_moves = []

    # Iterate over numbers 1 to 9
    for move in range(1, 10):
        move_str = str(move)  # Convert the move to a string
        row, col = MOVE_MAP[move_str]  # Get the row and column from MOVE_MAP
        cell_value = board[row][col]  # Get the value at that board position
        
        # Check if the cell is empty (not 'X' or 'O')
        if cell_value not in ["X", "O"]:
            available_moves.append(move_str)  # Add this move to available moves list

    # If no available moves, return
    if not available_moves:
        return

    # Initialize a dictionary to track the success rate of each move
    move_success_rate = {move: 0 for move in available_moves}
    
    # Analyze old data to populate move_success_rate
    for data in game_data:
        prev_board = data.get('board', [])
        outcome = data.get('outcome', None)
        
        # Check if the board state matches any old state and outcome is present
        if not outcome:
            continue  # Skip if outcome key is missing or None
        
        for move in available_moves:
            row, col = MOVE_MAP[move]
            if prev_board[row][col] == ' ':
                continue

            # Calculate the success rate for this move
            if outcome == "X":
                if prev_board[row][col] == "X":
                    move_success_rate[move] += 1
            elif outcome == "O":
                if prev_board[row][col] == "O":
                    move_success_rate[move] += 1

    # Choose the move with the highest success rate
    best_move = max(move_success_rate, key=move_success_rate.get, default=None)
    
    if best_move:
        row, col = MOVE_MAP[best_move]
        board[row][col] = current_player  # Use the passed current_player variable



def get_file_path(filename):
    # Get the file path in the same directory as the Python file
    return os.path.join(os.path.dirname(__file__), filename)

def save_game_data(board, outcome, filename='game_data.json'):
    # Save the game data to a json file
    data = {
        'board': board,
        'outcome': outcome
    }
    
    # Check if file exists and read content
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                game_data = json.load(f)
            except json.JSONDecodeError:
                game_data = []
    else:
        game_data = []

    # Append new data
    game_data.append(data)

    # Write all game data back to the file
    with open(filename, 'w') as f:
        json.dump(game_data, f)

def load_game_data(filename='game_data.json'):
    # Load game data from a json file
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                game_data = json.load(f)
                return game_data
            except json.JSONDecodeError as e:
                print(f"Error decoding json data: {e}")
                return []
    return []

def main():
    # Main function to run the game.
    print("Welcome to Tic-Tac-Toe!")
    print("\nChoose game mode:")
    print("1. Play with AI")
    print("2. Play with a friend")

    while True:
        mode = input("Enter your choice (1 or 2): ")
        if mode in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    board = initialize_board()  # Initialize the board
    current_player = "X"  # Set initial player

    if mode == "1":  # Play with AI
        print("\nChoose your player symbol:")
        print("1. X")
        print("2. O")

        while True:
            player_choice = input("Enter your choice (1 or 2): ")
            if player_choice == "1":
                player, ai = "X", "O"
                break
            elif player_choice == "2":
                player, ai = "O", "X"
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

        print("\nYou are playing against AI.")
        while True:
            print_board(board)  # Print the current state of the board

            if current_player == player:  # Player's turn
                print("Your turn:")
                while True:
                    move = input("Enter your move (1-9): ")  # Get the player's move
                    if make_move(board, move, player):
                        break
            else:  # AI's turn
                print("AI's turn:")
                ai_move(board, ai)  # Pass the AI player symbol

            winner = check_winner(board)  # Check if there's a winner
            if winner:
                print_board(board)  # Print the board with the final move
                if winner == player:
                    print("Congratulations! You win!")
                else:
                    print("AI wins!")
                save_game_data(board, winner)  # Save the game data
                break

            if all(cell in ["X", "O"] for row in board for cell in row):  # Check for a tie
                print_board(board)  # Print the final board
                print("It's a tie!")
                save_game_data(board, "Tie")  # Save the game data
                break

            # Switch the current player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

    else:  # Play with a friend
        print("You are playing against a friend.")
        current_player = "X"  # Player X starts first
        while True:
            print_board(board)  # Print the current state of the board
            print(f"Player {current_player}'s turn:")

            while True:
                move = input("Enter your move (1-9): ")  # Get the player's move
                if make_move(board, move, current_player):
                    break

            winner = check_winner(board)  # Check if there's a winner
            if winner:
                print_board(board)  # Print the board with the final move
                print(f"Congratulations! Player {winner} wins!")
                save_game_data(board, winner)  # Save the game data
                break

            if all(cell in ["X", "O"] for row in board for cell in row):  # Check for a tie
                print_board(board)  # Print the final board
                print("It's a tie!")
                save_game_data(board, "Tie")  # Save the game data
                break

            # Switch the current player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

main()  # Start the game

