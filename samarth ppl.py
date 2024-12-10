import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        # Create buttons for the board
        for i in range(9):
            button = tk.Button(self.master, text="", width=10, height=3, font=("Arial", 24),
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, i):
        # If the square is already taken, do nothing
        if self.board[i] != "":
            return
        # Update the board and the button
        self.board[i] = self.current_player
        self.buttons[i].config(text=self.current_player)
        # Check for a win or a tie
        if self.check_win():
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.reset_game()
        elif "" not in self.board:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
        else:
            # Switch player
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Define winning combinations (index positions)
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        # Check each combination
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        # Reset the board for a new game
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

# Create the main window
root = tk.Tk()
game = TicTacToe(root)
# Run the Tkinter event loop
root.mainloop()
