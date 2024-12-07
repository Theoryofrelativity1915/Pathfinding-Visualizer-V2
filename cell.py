import pygame as py
from constants import SQUARE_SIZE, BLACK

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.pos = (row * SQUARE_SIZE, col * SQUARE_SIZE)

    def render(self, canvas):
        py.draw.rect(canvas, BLACK, (self.col * SQUARE_SIZE,
                                                  self.row * SQUARE_SIZE, SQUARE_SIZE,
                                                  SQUARE_SIZE))

