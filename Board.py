class Board:

    def __init__(self, size: int) -> None:
        self._size = size
        self._board = []

    def create_board(self):
        self._board = [['#']*self._size for _ in range(self._size)]

    def get_board(self) -> list:
        return (self._board)

    def get_size(self) -> int:
        return (self._size)

    def set_size(self, size) -> None:
        self._size = size

    def make_move(self, x: int, y: int, char: str) -> None:
        self._board[y][x] = char