from Board import Board

class AI:

    def __init__(self, board: Board) -> None:
        self._board = board

    def get_in_list(self, lst: list, char: str) -> tuple:
        size = 4
        g_index = []
        filtered_1 = list(filter(lambda l: len(l) == 5, lst))
        for i, l in enumerate(filtered_1):
            nl = [ch for x,y,ch in l]
            if len(nl) == nl.count('#') + nl.count(char):
                g_index.append(i)
        filtered_2 = [filtered_1[i] for i in g_index]
        while size > 0:
            for l in filtered_2:
                nl = [ch for x,y,ch in l]
                if nl.count(char) == size:
                    return (l)
            size -= 1
        return ([])

    def get_conv_point(self, lst: list, char: str) -> tuple:
        l = self.get_in_list(lst, char)
        if l == []:
            return (None, None)
        for x,y,ch in l:
            if ch == '#':
                return (x,y)
        return (None, None)

    def get_best_pos(self, char: str) -> tuple:
        for i in range(5, 1, -1):
            possib = self._board.checker(char, self._board.get_size(), i)
            for elem in possib:
                disp, (x, y) = elem
                stock = []

                if disp == 'v':
                    for k in range(-(5-i), 1):
                        mylist = []
                        for it in range(k, k+5):
                            if 0 <= y + it < self._board.get_size():
                                mylist.append((x, y+it, self._board.get_board()[y + it][x]))
                        stock.append(mylist) 
                    return (self.get_conv_point(stock, char), i)
    
                elif disp == 'h':
                    for k in range(-(5 - i), 1):
                        mylist = []
                        for it in range(k, k+5):
                            if 0 <= x + it < self._board.get_size():
                                mylist.append((x+it, y, self._board.get_board()[y][x + it]))
                        stock.append(mylist)
                    return (self.get_conv_point(stock, char), i)

                elif disp == 'fd':
                    for k in range(-(5-i), 1):
                        mylist = []
                        for it in range(k, k+5):
                            if 0 <= x + it < self._board.get_size() and 0 <= y + it < self._board.get_size():
                                mylist.append((x+it, y+it, self._board.get_board()[y + it][x + it]))
                        stock.append(mylist)
                    return (self.get_conv_point(stock, char), i)

                elif disp == 'sd':
                    for k in range(-(5-i), 1):
                        mylist = []
                        for it in range(k, k+5):
                            if 0 <= x + it < self._board.get_size() and 0 <= y - it < self._board.get_size():
                                mylist.append((x+it, y-it, self._board.get_board()[y - it][x + it]))
                        stock.append(mylist)
                    return (self.get_conv_point(stock, char), i)

        return ((None, None), -1)

    def get_best_move(self):
        pos_me, i_me = self.get_best_pos('X')
        if pos_me != (None, None) and (i_me == 4):
            return (pos_me)
        else:
            pos_adv, i_adv = self.get_best_pos('O')
            if pos_adv != (None, None):
                return (pos_adv)
            if pos_me != (None, None):
                return (pos_me)
        for i, lst in enumerate(self._board.get_board()):
            for j, lst in enumerate(self._board.get_board()[i]):
                if self._board.get_board()[i][j] == '#':
                    return (j, i)