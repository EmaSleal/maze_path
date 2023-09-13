import heapq

OBSTACLE = 1
INFINITY = float('inf')


class AStarSearch:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def manhattan_distance(self,current, end):
        return abs(current[0] - end[0]) + abs(current[1] - end[1])

    def find_shortest_path(self, grid, start, end):
        rows, cols = len(grid), len(grid[0])
        distances = {(i, j): INFINITY for i in range(rows) for j in range(cols)}
        distances[start] = 0
        priority_queue = [(0, start)]
        predecessors = {start: None}

        obstacles = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == OBSTACLE:
                    obstacles.append((i, j))

        while priority_queue:
            _, current = heapq.heappop(priority_queue)
            if current == end:
                return self.reconstruct_path(current, predecessors)

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                x, y = current[0] + dx, current[1] + dy
                if 0 <= x < rows and 0 <= y < cols:
                    if grid[x][y] == 1:
                        continue
                    neighbor = (x, y)
                    tentative_distance = distances[current] + 1
                    if tentative_distance < distances[neighbor]:
                        distances[neighbor] = tentative_distance
                        f_value = tentative_distance + self.manhattan_distance(neighbor, end)
                        heapq.heappush(priority_queue, (f_value, neighbor))
                        predecessors[neighbor] = current

        return None

    def reconstruct_path(self, current, predecessors):
        path = []
        while current is not None:
            path.append(current)
            current = predecessors[current]
        return path[::-1]
