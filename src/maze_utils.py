from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np


def find_start_end(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 2:
                start = (i, j)
            elif cell == 3:
                end = (i, j)
    return start, end


def plot_grid(grid, show=True):
    color_map = {
        0: np.array([1, 1, 1]),
        1: np.array([0, 0, 0]),
        2: np.array([0, 1, 0]),
        3: np.array([1, 0, 0]),
        4: np.array([0, 0, 1]),
        5: np.array([1, 1, 0]),
        6: np.array([1, 0, 1]),
        7: np.array([0, 1, 1]),
        8: np.array([0.5, 0.5, 0.5]),
    }

    rows, cols = len(grid), len(grid[0])
    rgb_grid = np.zeros((rows, cols, 3))

    for i in range(rows):
        for j in range(cols):
            cell_value = grid[i][j]
            rgb_grid[i, j] = color_map[cell_value]

    plt.imshow(rgb_grid)
    plt.axis('off')

    if show:
        plt.show()


def visualize_route(grid, path, color_id):
    for row, col in path[1:-1]:
        grid[row][col] = color_id
        plot_grid(grid, show=False)

    plot_grid(grid)


def init_rgb_grid(rows, cols, subgrid_size, grid, color_map):
    rgb_grid = np.zeros((rows * subgrid_size, cols * subgrid_size, 3))
    for i in range(rows):
        for j in range(cols):
            cell_value = grid[i][j]
            rgb_grid[i * subgrid_size:(i + 1) * subgrid_size, j * subgrid_size:(j + 1) * subgrid_size] = color_map[
                cell_value]
    return rgb_grid


def update_rgb_grid_for_paths(rgb_grid, path_color_tuples, step, subgrid_size, color_map, end):
    for path_id, (path, color_id) in enumerate(path_color_tuples):
        if step < len(path):
            row, col = path[step]
            if (row, col) != end:
                dx = path_id % subgrid_size
                rgb_grid[row * subgrid_size + dx, col * subgrid_size:(col + 1) * subgrid_size] = color_map[color_id]


def visualize_multiple_routes(grid, path_color_tuples, end):
    color_map = {
        0: np.array([1, 1, 1]),
        1: np.array([0, 0, 0]),
        2: np.array([1, 1, 0]),
        3: np.array([0, 1, 0]),
        4: np.array([0, 0, 1]),
        5: np.array([1, 0, 1]),
        6: np.array([1, 0, 0]),
        7: np.array([0, 1, 1]),
        8: np.array([0.2, 0.2, 0.2]),
    }

    rows, cols = len(grid), len(grid[0])
    cell_route_count = defaultdict(int)

    for path, _ in path_color_tuples:
        for row, col in path:
            cell_route_count[(row, col)] += 1

    subgrid_size = max(cell_route_count.values())

    rgb_grid = init_rgb_grid(rows, cols, subgrid_size, grid, color_map)

    plt.imshow(rgb_grid)
    plt.axis('off')

    max_steps = max(len(path) for path, _ in path_color_tuples)

    for step in range(1, max_steps):
        update_rgb_grid_for_paths(rgb_grid, path_color_tuples, step, subgrid_size, color_map, end)

    plt.imshow(rgb_grid)
    plt.axis('off')
    plt.show()
