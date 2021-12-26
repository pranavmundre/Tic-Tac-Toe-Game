import os
import numpy as np


class TicTacToe:
    Board = np.array([[' ' for i in range(3)] for i in range(3)])
    opponent = ('computer', 'friend')

    def __init__(self):
        pass

    def start_game(self):
        self.display_grid()
        for i in range(9):
            if i % 2 == 0:
                player = 'X'
            else:
                player = 'O'
            print(f"'{player}' turn: Enter pos no: ", end="")
            while True:
                try:
                    pos = int(input()) - 1
                    if pos > 8:
                        print("Invalid position enter correct position: ", end="")
                        print("Already filled enter correct position: ", end="")
                        continue
                    x, y = int(pos / 3), pos % 3
                    if self.Board[x, y] == ' ':
                        self.Board[x, y] = str(player)
                        break
                    else:
                        print("Already filled enter correct position: ", end="")
                except ValueError:
                    print("[x]Enter integer value only.")

            self.display_grid()
            if self.game_result(player):
                print(f"Player '{player}' win the game.")
                break

    def display_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Play Tic Tac Toe Game")
        print("----------------------------------")
        DISPLAY = " {} | {} | {} ".format(self.Board[0, 0], self.Board[0, 1], self.Board[0, 2])
        DISPLAY += "\n___|___|___"
        DISPLAY += "\n {} | {} | {} ".format(self.Board[1, 0], self.Board[1, 1], self.Board[1, 2])
        DISPLAY += "\n___|___|___"
        DISPLAY += "\n {} | {} | {} ".format(self.Board[2, 0], self.Board[2, 1], self.Board[2, 2])
        DISPLAY += "\n   |   |   "
        print(DISPLAY)

    def game_result(self, player):
        win = False
        # horizontal
        if self.Board[0, 0] == self.Board[0, 1] == self.Board[0, 2] == player:
            win = True
        elif self.Board[1, 0] == self.Board[1, 1] == self.Board[1, 2] == player:
            win = True
        elif self.Board[2, 0] == self.Board[2, 1] == self.Board[2, 2] == player:
            win = True
        # vertical
        elif self.Board[0, 0] == self.Board[1, 0] == self.Board[2, 0] == player:
            win = True
        elif self.Board[0, 1] == self.Board[1, 1] == self.Board[2, 1] == player:
            win = True
        elif self.Board[0, 2] == self.Board[1, 2] == self.Board[2, 2] == player:
            win = True
        # diagonal
        elif self.Board[0, 0] == self.Board[1, 1] == self.Board[2, 2] == player:
            win = True
        elif self.Board[0, 2] == self.Board[1, 1] == self.Board[2, 0] == player:
            win = True

        return win


if '__main__' == __name__:
    try:
        obj = TicTacToe()
        obj.start_game()
    except KeyboardInterrupt:
        print("\nExit.")
