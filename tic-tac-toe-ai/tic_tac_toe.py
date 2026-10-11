"""A friendly, keyboard-accessible Tic-Tac-Toe game built with Tkinter."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class TicTacToe:
    """Manage the game state and its Tkinter user interface."""

    BOARD_SIZE = 3
    WINNING_LINES = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f7fb")

        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        self.buttons: list[ttk.Button] = []

        self._build_interface()
        self._bind_keyboard_controls()
        self._update_status()

    def _build_interface(self) -> None:
        """Create the board, status message, and game controls."""
        main = ttk.Frame(self.root, padding=20)
        main.grid(row=0, column=0)

        ttk.Label(
            main,
            text="Tic-Tac-Toe",
            font=("Segoe UI", 24, "bold"),
        ).grid(row=0, column=0, columnspan=3, pady=(0, 4))

        ttk.Label(
            main,
            text="Two players • X goes first",
            font=("Segoe UI", 10),
        ).grid(row=1, column=0, columnspan=3, pady=(0, 12))

        self.status = ttk.Label(
            main,
            text="",
            anchor="center",
            font=("Segoe UI", 12, "bold"),
        )
        self.status.grid(row=2, column=0, columnspan=3, pady=(0, 14))

        board_frame = ttk.Frame(main)
        board_frame.grid(row=3, column=0, columnspan=3)

        for index in range(9):
            button = ttk.Button(
                board_frame,
                text=" ",
                width=5,
                command=lambda position=index: self.play(position),
            )
            button.grid(
                row=index // self.BOARD_SIZE,
                column=index % self.BOARD_SIZE,
                padx=3,
                pady=3,
                ipady=12,
            )
            self.buttons.append(button)

        ttk.Button(
            main,
            text="New Game",
            command=self.new_game,
        ).grid(row=4, column=0, columnspan=3, pady=(16, 0))

        ttk.Label(
            main,
            text="Tip: use the number keys 1–9 to choose a square.",
            font=("Segoe UI", 9),
        ).grid(row=5, column=0, columnspan=3, pady=(10, 0))

    def _bind_keyboard_controls(self) -> None:
        """Allow number keys as an alternative to clicking a square."""
        for key, position in zip("123456789", range(9)):
            self.root.bind(key, lambda _event, p=position: self.play(p))
        self.root.bind("<Return>", lambda _event: self.new_game())
        self.root.bind("<Escape>", lambda _event: self.new_game())

    def play(self, position: int) -> None:
        """Place the current player's mark when the selected square is valid."""
        if self.game_over or not 0 <= position < len(self.board):
            return
        if self.board[position]:
            self.status.configure(text="That square is already taken. Choose another one.")
            return

        self.board[position] = self.current_player
        self.buttons[position].configure(text=self.current_player)

        winner = self._winner()
        if winner:
            self.game_over = True
            self.status.configure(text=f"Player {winner} wins! 🎉")
            self._disable_board()
        elif all(self.board):
            self.game_over = True
            self.status.configure(text="It's a draw! Great game.")
            self._disable_board()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self._update_status()

    def _winner(self) -> str | None:
        """Return the winning mark, or None if there is no winner yet."""
        for first, second, third in self.WINNING_LINES:
            if self.board[first] and self.board[first] == self.board[second] == self.board[third]:
                return self.board[first]
        return None

    def _update_status(self) -> None:
        self.status.configure(text=f"Player {self.current_player}'s turn")

    def _disable_board(self) -> None:
        for button in self.buttons:
            button.state(["disabled"])

    def new_game(self) -> None:
        """Reset the board and begin a new game with X."""
        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False
        for button in self.buttons:
            button.configure(text=" ")
            button.state(["!disabled"])
        self._update_status()


def main() -> None:
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()
