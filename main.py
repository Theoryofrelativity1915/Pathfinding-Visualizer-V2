# Example file showing a basic pygame "game loop"
import pygame as py
from constants import ROWS, COLS
from grid import Grid
from utilities import handle_click


def get_user_input_to_choose_algorithm():
    print("Hello! Please choose an algorithm \
        from the following search algorithms: ")
    print("1. Dijkstra")
    print("2. BFS")
    print("3. DFS")
    print("4. A Star")
    selected_algo = None
    while selected_algo is None:
        selected_algo = input("Please enter a number 1-4: ")
        if not (0 < int(selected_algo) < 5):
            selected_algo = None
    return selected_algo


# algorithm = int(get_user_input_to_choose_algorithm())
algorithm = 2
# pygame setup
py.init()
clock = py.time.Clock()
running = True
grid = Grid(ROWS, COLS)
start, end = None, None


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            start, end = handle_click(start, end)
            if start == end:
                end = None
                continue
            grid.set_start(start)
            grid.set_end(end)
        elif (event.type == py.KEYDOWN and event.key == py.K_SPACE and
              start is not None and end is not None):
            if algorithm == 1:
                print("Running Dijkstra's Algorithm")
                grid.dijkstra()
            elif algorithm == 2:
                print("Running BFS")
                grid.bfs()
            elif algorithm == 3:
                print("Running DFS")
                grid.dfs()
            elif algorithm == 4:
                print("Running A Star Algorithm")
                grid.A_Star()

    grid.render()
    clock.tick(60)  # limits FPS to 60

py.quit()
