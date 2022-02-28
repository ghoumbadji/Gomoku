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
                _input = input().strip()
                if _input != "":
                    command(self._board, _input.split(), self._error_cmd, self._info)
                    if _input == "END":
                        break
            except EOFError:
                break

if __name__ == "__main__":
    game = Gomoku()
    game.run()
