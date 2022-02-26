from Board import Board
import random

class AI:

    def __init__(self, board: Board) -> None:
        self._board = board

    def get_best_move(self) -> tuple:
        while True:
            x = random.randint(0, self._board.get_size() - 1)
            y = random.randint(0, self._board.get_size() - 1)
            if self._board.get_board()[y][x] == '#':
                return ((x,y))