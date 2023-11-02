from graph import Graph
from algorithms import bfs, find_diameter


# 9 вершин
VERTEXES: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

# 13 дуг
EDGES_1: list[list[str]] = [
    ["A", "B"],
    ["A", "C"],
    ["A", "D"],
    ["B", "E"],
    ["B", "H"],
    ["C", "E"],
    ["C", "F"],
    ["D", "F"],
    ["E", "G"],
    ["E", "I"],
    ["F", "G"],
    ["G", "I"],
    ["H", "I"]
]

EDGES_2: list[list[str]] = [
    ["A", "B"],
    ["A", "C"],
    ["A", "D"],
    ["B", "C"],
    ["D", "C"],
    ["C", "E"],
    ["E", "F"],
    ["E", "H"],
    ["F", "G"],
    ["F", "I"],
    ["H", "G"],
    ["H", "I"]
]

data = [str]


def __init_graph() -> Graph:
    g = Graph(len(VERTEXES))

    for edge in EDGES_2:
        g.add_edge(edge[0], edge[1])

    return g


if __name__ == "__main__":
    graph = __init_graph()

    graph.display_matrix()

    # Поиск в ширину для каждой из вершин
    for vertex in VERTEXES:
        bfs(graph, vertex)

        # Словарь vertex_routes содержит маршруты для конкретной вершины vertex
        graph.all_routes[vertex] = graph.vertex_routes

    graph_diameter = find_diameter(graph)
    print(f"Диаметр графа: {graph_diameter}", end="\n\n")

    #Вывод всех диаметральных маршрутов
    graph.display_routes(graph_diameter)
