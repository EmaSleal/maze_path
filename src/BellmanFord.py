from collections import deque


class BellmanFord:
    """Clase para implementar el algoritmo de Bellman-Ford personalizado."""

    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        self.distances = {}
        self.predecessors = {}

    def initialize(self, grid, start):
        """Inicializa las variables necesarias."""
        self.num_rows, self.num_cols = len(grid), len(grid[0])
        self.distances = {(i, j): float('inf') for i in range(self.num_rows) for j in range(self.num_cols)}
        self.distances[start] = 0
        self.predecessors = {start: None}

    from collections import deque

    def find_shortest_path(self, grid, start, end):
        self.initialize(grid, start)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([start])

        while queue:
            current = queue.popleft()

            for dx, dy in directions:
                x, y = current[0] + dx, current[1] + dy
                neighbor = (x, y)

                if 0 <= x < self.num_rows and 0 <= y < self.num_cols and grid[x][y] != 1:
                    new_distance = self.distances[current] + 1
                    if new_distance < self.distances[neighbor]:
                        self.distances[neighbor] = new_distance
                        self.predecessors[neighbor] = current
                        queue.append(neighbor)

        if self.distances[end] == float('inf'):
            return None

        return self.reconstruct_path(end)

    def reconstruct_path(self, end):
        """Reconstruye el camino más corto."""
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = self.predecessors.get(current, None)
        return path[::-1] if path else None
