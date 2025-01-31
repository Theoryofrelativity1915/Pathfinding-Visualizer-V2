from constants import ROWS, COLS, SQUARE_SIZE
import pygame as py


def get_row_col_from_pos(x, y):
    return (x // SQUARE_SIZE, y // SQUARE_SIZE)


def handle_click(start, end):
    x, y = py.mouse.get_pos()
    row, col = get_row_col_from_pos(x, y)
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        return (None, None)
    elif not start:  # Only start has been selected
        start = (col, row)
    elif not end:  # Both start and end have been selected
        end = (col, row)
    return (start, end)
