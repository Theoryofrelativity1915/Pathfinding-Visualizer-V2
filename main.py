# Example file showing a basic pygame "game loop"
import pygame as py
from algorithms.dfs import dfs
from constants import ROWS, COLS
from grid import Grid

# pygame setup
py.init()
clock = py.time.Clock()
running = True
grid = Grid(ROWS, COLS)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    grid.render()
    dfs(grid,grid.grid[0][0], grid.grid[10][10])
    clock.tick(60)  # limits FPS to 60

py.quit()
