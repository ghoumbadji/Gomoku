from Board import Board
from AI import AI
from Info import Info

class Command:

    def __init__(self, cmd: str) -> None:
        self._cmd = cmd

    def get_cmd(self) -> str:
        return (self._cmd)

    def set_cmd(self, cmd: str) -> None:
        self._cmd = cmd


    # Mandatory commands

    def start(self, board: Board, size: int) -> None:
        if size >= 5:
            board.set_size(size)
            print("OK", flush=True)
        else:
            self.error("unsupported size")
       
    def turn(self, board: Board, x: int, y: int) -> None:
        board.make_move(x, y, 'O')
        ai = AI(board)
        x, y = ai.get_best_move()
        board.make_move(x, y, 'X')
        print(f"{x},{y}", flush=True)

    def begin(self, board: Board) -> None:
        board.make_move(2, 2, 'X')
        print("2,2", flush=True)

    def board_cmd(self, board: Board) -> None:
        corres = {1: 'X', 2: 'O'}
        board.set_size(board.get_size())
        while True:
            _input = input()
            _input = _input.strip()
            _input = _input.replace('\\r', '')
            _input = _input.replace('\\n', '')

            if _input == "":
                pass
            elif _input == "DONE":
                ai = AI(board)
                x, y = ai.get_best_move()
                board.make_move(x, y, 'X')
                print(f"{x},{y}", flush=True)
                break
            else:
                lst = _input.split(",")
                if len(lst) != 3:
                    self.error("Invalid input for board")
                else:
                    try:
                        arg_nbr = list(map(int, lst))
                        if not (0 <= arg_nbr[0] < board.get_size()) or not (0 <= arg_nbr[1] < board.get_size()):
                            self.error("Invalid range for coordinate(s)")
                        elif arg_nbr[2] not in [1,2]:
                            self.error("Last number should be 1 or 2")
                        elif board.get_board()[arg_nbr[1]][arg_nbr[0]] != '#':
                            self.error("Position already taken")
                        else:
                            board.make_move(arg_nbr[0], arg_nbr[1], corres[arg_nbr[2]])
                    except ValueError:
                       self.error("Invalid input for board")


    def info(self, info: Info, key: str, value: int) -> None:
        info.set_value(key, value)

    def about(self) -> None:
        print("name='GomoBrain, version='1.0', author='Da.Ge.Mo', country='BJ'", flush=True)

    def end(self) -> None:
        pass



    # optional commands

    def recstart(self, board: Board, width: int, height: int) -> None:
        print(flush=True)

    def restart(self, board: Board) -> None:
        board.set_size(board.get_size())
        print ("OK", flush=True)

    def takeback(self, board: Board, x: int, y: int) -> None:
        tab = board.get_board()
        board.get_board()[y][x] = '#'
        print("OK", flush=True)

    def play(self, board: Board, x: int, y: int) -> None:
        print(flush=True)


    # error commands

    def unknown(self, msg: str) -> None:
        print(f"UNKNOWN {msg}", flush=True)

    def error(self, msg: str) -> None:
        print(f"ERROR {msg}", flush=True)

    def message(self, msg: str) -> None:
        print(f"MESSAGE {msg}", flush=True)

    def debug(self, board: Board, msg: str) -> None:
        print(f"DEBUG {msg}", flush=True)

    def suggest(self, board: Board, x: int, y: int) -> None:
        print(f"SUGGEST {x},{y}", flush=True)



    # process string

    def process(self, board: Board, info: Info) -> None:
        validCmds = ["START", "TURN", "BEGIN", "BOARD", "INFO", "END", "ABOUT", "RESTART"]

        if (self._cmd.split())[0] not in validCmds:
            self.unknown(self._cmd)

        if "ABOUT" in self._cmd:
            if self._cmd != "ABOUT":
                self.error("Invalid use of ABOUT command") 
            else:
                self.about()

        if "START" in self._cmd and "RE" not in self._cmd:
            args = self._cmd.split()
            if len(args) == 2:
                try:
                    nbr = int(args[1])
                    self.start(board, nbr)
                except ValueError:
                    self.error("Invalid use of START command")
            else:
                self.error("Invalid use of START command")

        if "RESTART" in self._cmd:
            if self._cmd != "RESTART":
                 self.error("Invalid use of RESTART command")
            else:
                self.restart(board)

        if "TURN" in self._cmd:
            args = self._cmd.split()
            if len(args) == 2:
                args_in = args[1].split(',')
                if len(args_in) == 2:
                    try:
                        arg_nbr = list(map(int, args_in))
                        if not (0 <= arg_nbr[0] < board.get_size()) or not(0 <= arg_nbr[1] < board.get_size()):
                            self.error("Invalid range for coordinate(s)")
                        elif board.get_board()[arg_nbr[1]][arg_nbr[0]] == '#':
                            self.turn(board, arg_nbr[0], arg_nbr[1])
                        else:
                            self.error("Position already taken")
                    except ValueError:
                        self.error("Invalid use of TURN command")

                else:
                    self.error("Invalid use of TURN command")
            else:
                self.error("Invalid use of TURN command")

        if "BEGIN" in self._cmd:
            if "BEGIN" != self._cmd:
                self.error("Invalid use of BEGIN command")
            else:
                self.begin(board)

        if "BOARD" in self._cmd:
            if "BOARD" != self._cmd:
                self.error("Invalid use of BOARD command")
            else:
                self.board_cmd(board)

        if "INFO" in self._cmd:
            args = self._cmd.split()
            if len(args) != 3:
                self.error("Invalid use of INFO command")
            else:
                try:
                    if args[2] != "folder":
                        val = int(args[2])
                    else:
                        val = args[2]
                    self.info(info, args[1], val)
                except ValueError:
                    self.error("Invalid use of INFO command")

        if "END" in self._cmd:
            if self._cmd != "END":
                self.error("Invalid use of END command")
            else:
                self.end()

