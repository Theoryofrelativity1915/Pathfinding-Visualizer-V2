import pygame as py
from math import sqrt
from constants import SQUARE_SIZE, BLACK, GREEN, BLUE, WHITE, RED


def manhattan_dist(current_cell, destination_cell):
    sqrt((destination_cell.row - current_cell.row) ^ 2 +
         (destination_cell.col - current_cell.col) ^ 2)


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.pos = (row * SQUARE_SIZE, col * SQUARE_SIZE)
        self.f_cost = None
        self.parent = None  # used to recreate path
        self.is_start = False
        self.is_end = False
        self.color = WHITE
        self.visited = False

    def render(self, canvas):
        if self.is_start:
            self.color = GREEN
        elif self.is_end:
            self.color = BLUE
        elif self.visited:
            self.color = RED
        else:
            self.color = WHITE
        py.draw.rect(canvas, self.color, (self.col * SQUARE_SIZE,
                                          self.row * SQUARE_SIZE, SQUARE_SIZE,
                                          SQUARE_SIZE))

    def calc_f_cost(self):
        pass
