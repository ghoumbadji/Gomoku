from Board import Board
from AI import AI
from Info import Info
import random

class ErrorCommand:

    def __init__(self) -> None:
        pass

    def unknown(self, msg: str) -> None:
        print(f"UNKNOWN {msg}", flush=True)

    def error(self, msg: str) -> None:
        print(f"ERROR {msg}", flush=True)

    def message(self, msg: str) -> None:
        print(f"MESSAGE {msg}", flush=True)

    def debug(self, msg: str) -> None:
        print(f"DEBUG {msg}", flush=True)

    def suggest(self, x: int, y: int) -> None:
        print(f"SUGGEST {x},{y}", flush=True)


def start(board: Board, params: list, error_cmd: ErrorCommand, info: Info) -> None:
    if len(params) != 1:
        error_cmd.error("bad use of START command")
    else:
        try:
            size = int(params[0])
            if size < 5:
                error_cmd.error("unsupported size")
            else:
                board.set_size(size)
                board.create_board()
                print("OK", flush=True)
        except ValueError:
            error_cmd.error("invalid size")


def restart(board: Board, params: list, error_cmd: ErrorCommand, info: Info) -> None:
    if len(params) != 0:
        error_cmd.error("bad use of RESTART command")
    else:
        board.set_size(board.get_size())
        board.create_board()
        print("OK", flush=True)


def turn(board: Board, params: list, error_cmd: ErrorCommand, info: Info) -> None:
    if len(params) != 1:
        error_cmd.error("bad use of TURN command")
    else:
        args_in = params[0].split(',')
        if len(args_in) != 2:
            error_cmd.error("invalid coordinate(s)")
        else:
            try:
                arg_nbr = list(map(int, args_in))
                size = board.get_size()
                if not (0 <= arg_nbr[0] < size) or not (0 <= arg_nbr[1] < size):
                    error_cmd.error("invalid range for coordinate(s)")
                elif board.get_board()[arg_nbr[1]][arg_nbr[0]] != '#':
                    error_cmd.error("Position already taken")
                else:
                    board.make_move(arg_nbr[0], arg_nbr[1], 'O')
                    ai = AI(board)
                    x1, y1 = ai.get_best_move()
                    board.make_move(x1, y1, 'X')
                    print(f"{x1},{y1}", flush=True)
            except ValueError:
                error_cmd.error("invalid coordinate(s)")


def begin(board: Board, params: list, error_cmd: ErrorCommand, info: Info) -> None:
    if len(params) != 0:
        error_cmd.error("bad use of BEGIN command")
    else:
        x = random.randint(0, board.get_size() - 1)
        y = random.randint(0, board.get_size() - 1)
        board.make_move(x, y, 'X')
        print(f"{x},{y}", flush=True)


def board_cmd(board: Board, params: list, error_cmd: ErrorCommand, info: Info) -> None:
    corres = {1: 'X', 2: 'O'}
    board.set_size(board.get_size())
    board.create_board()
    if len(params) != 0:
        error_cmd.error("bad use of BOARD command")
    else:
        while True:
            try:
                _input = input().strip()
                if _input == "":
                    continue
                elif _input == "DONE":
                    break
                else:
                    lst = _input.split(",")
                if len(lst) != 3:
                    error_cmd.error("Invalid input for board")
                else:
                    try:
                        arg_nbr = list(map(int, lst))
                        size = board.get_size()
                        if not (0 <= arg_nbr[0] < size) or not (0 <= arg_nbr[1] < size):
                            error_cmd.error("Invalid range for coordinate(s)")
                        elif arg_nbr[2] not in [1, 2]:
                            error_cmd.error("Last number should be 1 or 2")
                        elif board.get_board()[arg_nbr[1]][arg_nbr[0]] != '#':
                            error_cmd.error("Position already taken")
                        else:
                            board.make_move(
                                arg_nbr[0], arg_nbr[1], corres[arg_nbr[2]])
                    except ValueError:
                        error_cmd.error("Invalid input for board")
            except EOFError:
                break
    ai = AI(board)
    x, y = ai.get_best_move()
    board.make_move(x, y, 'X')
    print(f"{x},{y}", flush=True)


def info_cmd(board: Board, params: list, error_cmd: ErrorCommand, info: Info) -> None:
    if len(params) != 2:
        error_cmd.error("invalid use of INFO command")
    else:
        keys = info.get_valid_keys()
        if params[0] not in keys:
            error_cmd.error("invalid key")
        else:
            key = params[0]
            try:
                value = int(params[1]) if key != "folder" else params[1]
                info.set_value(key, value)
            except ValueError:
                error_cmd.error("invalid input")


def about(board: Board, params: list, error_cmd: ErrorCommand, info: Info) -> None:
    if len(params) != 0:
        error_cmd.error("invalid use of ABOUT command")
    else:
        print("name='GomoBrain, version='1.0', author='Da.Ge.Mo', country='BJ'", flush=True)


def end(board: Board, params: list, error_cmd: ErrorCommand, info: Info) -> None:
    if len(params) != 0:
        error_cmd.error("invalid use of END command")
    else:
        pass


def command(board: Board, args: list, error_cmd: ErrorCommand, info: Info) -> None:
    command_map = {
        "START": start,
        "RESTART": restart,
        "TURN": turn,
        "BEGIN": begin,
        "BOARD": board_cmd,
        "ABOUT": about,
        "END": end,
    }
    if args[0] in command_map.keys():
        command_map[args[0]](board, args[1:], error_cmd, info)
