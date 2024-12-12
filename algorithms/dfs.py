def dfs(grid, start_vertex, end_vertex):
    dfs_helper(start_vertex, end_vertex)

def dfs_helper(vertex, end_vertex):
    if vertex == end_vertex or vertex is None or vertex.visit == True:
        return
    vertex.visit = True
    for neighbor in vertex.neighbors:
        dfs_helper(neighbor, end_vertex)
        neighbor.visit = True


