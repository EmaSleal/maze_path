from collections import deque

class BreadthFirstSearch:
    """Clase para implementar el algoritmo de búsqueda en anchura (BFS) modificado."""

    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        self.previous_nodes = {}
        self.POSSIBLE_MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.COSTS = {
            (0, 1): 1.0,
            (1, 0): 1.0,
            (0, -1): 1.0,
            (-1, 0): 1.0
        }

    def setup(self, grid):
        """Inicializa las variables necesarias."""
        self.num_rows, self.num_cols = len(grid), len(grid[0])
        self.previous_nodes = {}

    def find_shortest_path(self, grid, start, end, max_distance=None):
        """Encuentra una ruta en una cuadrícula entre un punto de inicio y un punto final."""
        self.setup(grid)
        return self.modified_bfs(grid, start, end, max_distance)

    def modified_bfs(self, grid, start, end, max_distance=None):
        """Realiza la búsqueda en anchura modificada."""
        queue = deque([(start, 0)])
        self.previous_nodes[start] = None

        while queue:
            current, distance = queue.popleft()
            if current == end:
                return self.reconstruct_path(current)

            if max_distance is not None and distance >= max_distance:
                continue

            for dx, dy in self.POSSIBLE_MOVES:
                x, y = current[0] + dx, current[1] + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    neighbor = (x, y)
                    if neighbor in self.previous_nodes or grid[x][y] == 1:
                        continue
                    queue.append((neighbor, distance + 1))
                    self.previous_nodes[neighbor] = current

        return None

    def reconstruct_path(self, current):
        """Reconstruye la ruta."""
        path = []
        while current is not None:
            path.append(current)
            current = self.previous_nodes.get(current, None)
        return path[::-1]
