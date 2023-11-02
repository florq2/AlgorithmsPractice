class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = {}
        self.vertex_routes = {}
        self.all_routes = {}

        for vertex in range(vertices):
            self.matrix[chr(ord('A') + vertex)] = {}
            for other_vertex in range(vertices):
                self.matrix[chr(ord('A') + vertex)][chr(ord('A') + other_vertex)] = 0

    def add_edge(self, start, end):
        if start in self.matrix and end in self.matrix:
            self.matrix[start][end] = 1
            self.matrix[end][start] = 1

    def get_neighbors(self, vertex) -> list:
        if vertex in self.matrix:
            return [neighbor for neighbor, connected in self.matrix[vertex].items() if connected == 1]
        else:
            return []

    def display_matrix(self):
        vertices = list(self.matrix.keys())
        print(" ", " ".join(vertices))
        for vertex in vertices:
            print(vertex, end=" ")
            for other_vertex in vertices:
                print(self.matrix[vertex][other_vertex], end=" ")
            print()
        print()

    def display_routes(self, length):
        for source, destinations in self.all_routes.items():
            print(f"Маршруты для вершины {source}:")
            for vertex, routes in destinations.items():
                route_str = ""
                for destination, route in routes.items():
                    route_str += destination + ' -> '

                if len(route_str) > 6 * length:
                    print(f"До вершины {vertex}:")
                    print(route_str[:-3])
            print()