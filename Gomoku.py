#!/usr/bin/python3

from Board import Board
from Commands.command import command
from Commands.ErrorCommand import ErrorCommand
from Info import Info

class Gomoku:

    def __init__(self) -> None:
        self._board = Board(20)
        self._error_cmd = ErrorCommand()
        self._info = Info()

    def run(self) -> None:
        while (True):
            try:
                _input = input()
                _input = _input.strip().replace('\\r', '').replace('\\n', '')
                if _input != "":
                    ret = command(self._board, _input.split(), self._error_cmd, self._info)
                    if ret == 1:
                        break
            except EOFError:
                break

if __name__ == "__main__":
    game = Gomoku()
    game.run()
