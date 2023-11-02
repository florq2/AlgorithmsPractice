from collections import deque
from graph import Graph


def bfs(g: Graph, start):
    g.vertex_routes = {}
    visited = {vertex: False for vertex in g.matrix.keys()}
    queue = deque()
    queue.append(start)
    visited[start] = True

    routes_per_vertex = {start: {start: [start]}}

    while queue:
        vertex = queue.popleft()
        neighbors = g.get_neighbors(vertex)
        for neighbor in neighbors:
            if not visited[neighbor]:
                new_route = routes_per_vertex[vertex].copy()
                new_route[neighbor] = new_route.get(neighbor, []) + [neighbor]
                routes_per_vertex[neighbor] = new_route
                queue.append(neighbor)
                visited[neighbor] = True

    g.vertex_routes = routes_per_vertex


def find_diameter(g: Graph):
    max_diameter = 0

    for i in g.matrix.keys():
        for k in g.matrix.keys():
            cur_len = len(g.all_routes[i][k])
            if cur_len > max_diameter:
                max_diameter = cur_len

    # Вычитаем 1, т.к. в all_routers учитывается сама вершина
    return max_diameter - 1
