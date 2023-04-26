class Reversi:
    def __init__(self) -> None:
        self.dirs = [-10, -9, -8, -1, 1, 8, 9, 10]
        self.discs = " - o x\n"
        self.board = [0 if i % 9 else 3 for i in range(91)]
        self.board[40] = self.board[50] = self.turn = 1
        self.board[41] = self.board[49] = 2

    def _check(self, board, move, flip=False):
        if not (ret := False) and not board[move]:
            pass
        return ret
