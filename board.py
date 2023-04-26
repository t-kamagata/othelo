EMPTY = "."
BLACK = "#"
WHITE = "o"
WALL = 3

class Board:
    def __init__(self) -> None:
        self.turn = BLACK
        self.cnt_reversable = [[0 for _ in range(8)] for _ in range(8)]
        self.board = [[EMPTY for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                horizontalEdge = i == 0 or i == 8
                verticalEdge = j == 0 or j == 8
                if horizontalEdge or verticalEdge:
                    self.board[i][j] = WALL
        self.board[3][3] = BLACK
        self.board[3][4] = WHITE
        self.board[4][3] = WHITE
        self.board[4][4] = BLACK
        self.update_reversable()
    
    def update_reversable(self):
        for i in range(1, 7):
            for j in range(1, 7):
                count_sum = 0
                for dir in range(8):
                    (x, y) = self.indexToVec2(dir)
                    if self.turn == WHITE:
                        if self.board[i+x][j+y] == BLACK:
                            count = 1
                            while True:
                                if self.board[i + (x*count)][j + (y*count)] == EMPTY or\
                                self.board[i + (x*count)][j + (y*count)] == WALL:
                                    self.cnt_reversable[i][j] = count_sum
                                    break
                                elif self.board[i + (x*count)][j + (y*count)] == WHITE:
                                    count_sum += count-1
                                    self.cnt_reversable[i][j] = count_sum
                                    break
                                else:
                                    count += 1
                        else:
                            self.cnt_reversable[i][j] = count_sum
                    else:
                        if self.board[i+x][j+y] == WHITE:
                            count = 1
                            while True:
                                if self.board[i + (x*count)][j + (y*count)] == EMPTY or\
                                self.board[i + (x*count)][j + (y*count)] == WALL:
                                    self.cnt_reversable[i][j] = count_sum
                                    break
                                elif self.board[i + (x*count)][j + (y*count)] == BLACK:
                                    count_sum += count-1
                                    self.cnt_reversable[i][j] = count_sum
                                    break
                                else:
                                    count += 1
                        else:
                            self.cnt_reversable[i][j] = count_sum
    
    def puttable(self, x, y):
        return self.cnt_reversable[x][y] > 0
    
    def put(self, i, j):
        for dir in range(8):
            (x, y) = self.indexToVec2(dir)
            if self.turn == WHITE:
                if self.board[i+x][j+y] == BLACK:
                    count = 1
                    while True:
                        if self.board[i + (x*count)][j + (y*count)] == EMPTY or\
                        self.board[i + (x*count)][j + (y*count)] == WALL:
                            self.cnt_reversable[i][j] = 0
                            break
                        elif self.board[i + (x*count)][j + (y*count)] == WHITE:
                            for t in range(1, count):
                                self.board[i + (x*t)][j + (y*t)] = BLACK
                            break
                        else:
                            count += 1
                else:
                    self.cnt_reversable[i][j] = 0
            else:
                if self.board[i+x][j+y] == BLACK:
                    count = 1
                    while True:
                        if self.board[i + (x*count)][j + (y*count)] == EMPTY or\
                        self.board[i + (x*count)][j + (y*count)] == WALL:
                            self.cnt_reversable[i][j] = 0
                            break
                        elif self.board[i + (x*count)][j + (y*count)] == BLACK:
                            self.cnt_reversable[i][j] = count
                            break
                        else:
                            count += 1
                else:
                    self.cnt_reversable[i][j] = 0
    
    def flipTurn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def indexToVec2(self, i):
        if i == 0:
            return (0, 1) # 上
        elif i == 1:
            return (1, 1) # 右上
        elif i == 2:
            return (1, 0) # 右
        elif i == 3:
            return (1, -1) # 右下
        elif i == 4:
            return (0, -1) # 下
        elif i == 5:
            return (-1, -1) # 左下
        elif i == 6:
            return (-1, 0) # 左
        elif i == 7:
            return (-1, 1) # 左上
        else:
            return (0, 0)
        
    def print(self):
        print("  ", end="")
        for i in range(6):
            print(f"{i+1:^2}", end="")
        print("")

        for i in range(6):
            print(f"{i+1:^2}", end="")
            for j in range(6):
                print(f"{'p' if self.puttable(i+1, j+1) else self.board[i+1][j+1]:^2}", end="")
            print("")