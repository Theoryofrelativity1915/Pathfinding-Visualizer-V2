import pygame as py
from constants import BLACK, BLUE, SCREEN_SIZE, SQUARE_SIZE, COLS, ROWS
from cell import Cell


class Grid:
    def __init__(self, rows, cols):
        self.canvas = py.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        self.rows = rows
        self.cols = cols
        self.grid = self.init_grid_and_cells()
        self.start = None
        self.end = None
        self.visited = False

    def dijkstra(self):
        pass

    def outside_bounds(self, position):
        if position < 0 or position >= ROWS or position >= COLS:
            return True
        return False

    def bfs(self):
        q = []
        q.append((self.start.row, self.start.col))
        while len(q):
            row, col = q.pop(0)
            # print(row, col)
            if self.grid[row][col].visited:
                continue
            self.grid[row][col].visited = True
            self.grid[row][col].render(self.canvas)
            if self.grid[row][col] == self.end:
                print("Solution found!")
                return
            neighbors = [(row - 1, col), (row + 1, col),
                         (row, col - 1), (row, col + 1)]
            for neighbor in neighbors:
                curr_row, curr_col = neighbor
                if (self.outside_bounds(curr_row) or
                        self.outside_bounds(curr_col)):
                    continue
                elif self.grid[curr_col][curr_col].visited:
                    continue
                else:
                    self.grid[curr_col][curr_col].parent = self.grid[row][col]
                    q.append((curr_row, curr_col))
        return

    def dfs(self):
        path = []
        visited = set()

        def dfs_helper(row, col, path):
            print(row, col)
            self.render()
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS):
                return
            elif self.grid[row][col] == self.end:
                return path
            elif self.grid[row][col].visited:
                return
            else:
                # path.append((row - 1, col))
                dfs_helper(row - 1, col, path)
                # path.pop()
                # path.append((row + 1, col))
                dfs_helper(row + 1, col, path)
                # path.pop()
                # path.append((row, col - 1))
                dfs_helper(row, col - 1)
                # path.pop()
                # path.append((row, col + 1))
                dfs_helper(row, col + 1, path)
                # path.pop()
        start_row, start_col = self.start.row, self.start.col
        return dfs_helper(start_row, start_col, path)

    def A_Star(self):
        pass

    def init_grid_and_cells(self):
        board = []
        for r in range(self.rows):
            row = []
            for col in range(self.cols):
                cell = Cell(r, col)
                row.append(cell)
            board.append(row)
        return board

    def render(self):
        # fill the screen with a color to wipe away anything from last frame
        self.canvas.fill("WHITE")
        # flip() the display to put your work on screen
        self.draw_cells()
        py.display.flip()

    def draw_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                py.draw.line(self.canvas, BLACK, (0, row * SQUARE_SIZE),
                             (SCREEN_SIZE, row * SQUARE_SIZE))
                py.draw.line(self.canvas, BLUE, (col * SQUARE_SIZE,
                             0), (col * SQUARE_SIZE, SCREEN_SIZE))
                cell = self.grid[row][col]
                cell.render(self.canvas)

    def set_start(self, start_pos):
        if start_pos is None and self.start is None:
            return
        elif start_pos is None and self.start is not None:
            self.start.is_start = False
            self.start = None
        else:
            row, col = start_pos
            self.start = self.grid[row][col]
            self.start.is_start = True

    def set_end(self, end_pos):
        if end_pos is None and self.end is None:
            return
        elif end_pos is None and self.end is not None:
            self.end.is_end = False
            self.end = None
        else:
            row, col = end_pos
            self.end = self.grid[row][col]
            self.end.is_end = True
