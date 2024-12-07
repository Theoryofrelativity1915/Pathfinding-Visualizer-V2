import pygame as py
from constants import BLACK, BLUE, SCREEN_SIZE, SQUARE_SIZE
from cell import Cell
class Grid:
    def __init__(self, rows, cols):
        self.canvas = py.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        self.rows = rows
        self.cols = cols
        self.grid = self.init_grid_and_cells()

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
                py.draw.line(self.canvas, BLACK,(0, row * SQUARE_SIZE), (SCREEN_SIZE, row * SQUARE_SIZE))
                py.draw.line(self.canvas, BLUE,(col * SQUARE_SIZE, 0), (col * SQUARE_SIZE,SCREEN_SIZE))
