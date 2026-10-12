# Tkinter Tic-Tac-Toe

This project is a two-player Tic-Tac-Toe game built in Python with the Tkinter GUI module. Players take turns placing X and O on a 3-by-3 board. The program detects wins and draws, prevents players from selecting occupied squares, displays the current game status, and provides a button to start a new game. Players can use either the mouse or the number keys 1–9 to choose a square.

## Instructions for Build and Use

### Steps to build and/or run the software

1. Install Python 3.10 or newer.
2. Download or clone this project and open a terminal in the `tic-tac-toe-ai` folder.
3. Run the program with:

   ```bash
   python tic_tac_toe.py
   ```

   On some systems, use `python3 tic_tac_toe.py` instead.

### Instructions for using the software

1. Player X starts the game by clicking an empty square on the board, or by pressing a number key from 1 to 9.
2. Player O takes the next turn. Continue alternating turns until one player gets three marks in a row or the board is full.
3. When the game ends, read the result in the status message. Click **New Game**, or press Enter or Escape, to play again.

The number-key layout matches the board from left to right and top to bottom:

```text
1 2 3
4 5 6
7 8 9
```

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.10 or newer
* Tkinter, included with most standard Python installations
* Python standard library only; no third-party packages are required
* A code editor such as Visual Studio Code, IDLE, or PyCharm

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Python Official Documentation](https://docs.python.org/3/)
* [Tkinter GUI Programming](https://docs.python.org/3/library/tkinter.html)
* [Tkinter ttk Widgets](https://docs.python.org/3/library/tkinter.ttk.html)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add a single-player mode with an AI opponent.
* [ ] Add a scoreboard that tracks wins, losses, and draws.
* [ ] Add selectable difficulty levels for the AI opponent.
* [ ] Improve the visual design with highlighted winning squares and customizable themes.
* [ ] Add automated tests for win, draw, restart, and invalid-move behavior.
