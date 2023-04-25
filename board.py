EMPTY = "."
BLACK = "#"
WHITE = "o"
WALL = 3

class Board:
    def __init__(self) -> None:
        self.turn = BLACK
        self.board = [[EMPTY for _ in range(7)] for _ in range(7)]
        for i in range(7):
            for j in range(7):
                horizontalEdge = i == 0 or i == 7
                verticalEdge = j == 0 or j == 7
                if horizontalEdge or verticalEdge:
                    self.board[i][j] = WALL

    

    def print(self):
        print("  ", end="")
        for i in range(5):
            print(f"{i:^2}", end="")
        print("")

        for i in range(5):
            print(f"{i:^2}", end="")
            for j in range(5):
                print(f"{self.board[i+1][j+1]:^2}", end="")
            print("")