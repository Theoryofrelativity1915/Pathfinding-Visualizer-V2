from time import sleep
def dfs(grid, start_vertex, end_vertex):
    dfs_helper(start_vertex, end_vertex)

def dfs_helper(vertex, end_vertex):
    if vertex == end_vertex or vertex is None or vertex.visited == True:
        return
    vertex.visited = True
    for neighbor in vertex.neighbors:
        sleep(1)
        dfs_helper(neighbor, end_vertex)
        neighbor.visited = True


