class DepthFirstSearch:
    """Clase para implementar el algoritmo de búsqueda en profundidad (DFS) personalizado."""

    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        self.visited_nodes = set()
        self.predecessors = {}

    def initialize(self, grid):
        """Inicializa las variables necesarias."""
        self.num_rows, self.num_cols = len(grid), len(grid[0])
        self.visited_nodes = set()
        self.predecessors = {}

    def find_shortest_path(self, grid, start, end, max_depth=None):
        """Encuentra una ruta en una cuadrícula entre un punto de inicio y un punto final."""
        self.initialize(grid)
        return self.custom_dfs(grid, start, end, max_depth)

    def custom_dfs(self, grid, current, end, max_depth=None):
        """Realiza la búsqueda en profundidad personalizada."""
        if current == end:
            return self.reconstruct_path(current)

        if max_depth is not None and max_depth <= 0:
            return None

        self.visited_nodes.add(current)
        possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in possible_moves:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < self.num_rows and 0 <= y < self.num_cols:
                neighbor = (x, y)
                if neighbor in self.visited_nodes or grid[x][y] == 1:
                    continue
                self.predecessors[neighbor] = current
                path = self.custom_dfs(grid, neighbor, end, max_depth - 1 if max_depth is not None else None)
                if path:
                    return path

        return None

    def reconstruct_path(self, current):
        """Reconstruye la ruta."""
        path = []
        while current is not None:
            path.append(current)
            current = self.predecessors.get(current, None)
        return path[::-1]
