import os
from src.dijkstra import Dijkstra
from src.BellmanFord import BellmanFord
from src.DepthFirstSearch import DepthFirstSearch
from src.BreadthFirstSearch import BreadthFirstSearch
from src.AStarSearch import AStarSearch
from src.maze_utils import find_start_end, visualize_route, visualize_multiple_routes
from src.memory import measure_performance
from src.csv_utils import read_csv, save_to_csv

directorio_actual = os.path.dirname(__file__)
base_path = os.path.dirname(directorio_actual)
MAZE_PATH = "data/"
full_file_path = os.path.join(base_path, MAZE_PATH)
lista_archivos = os.listdir(full_file_path)


def main():
    while True:
        lista_archivos.remove('__init__.py')
        num = 1

        print("Bienvenido al programa de rutas más cortas.")
        print("Por favor, elige un laberinto:")
        for num, archivo in enumerate(lista_archivos, start=1):
            print(f"{num}. {archivo[:-4]}")

        choice = input("Tu elección: ")

        if choice == '7':
            print("Saliendo del programa.")
            break

        try:
            full_file_path = os.path.join(base_path, MAZE_PATH, lista_archivos[int(choice) - 1])

            algoritmos = {
                '1': Dijkstra,
                '2': BellmanFord,
                '3': DepthFirstSearch,
                '4': BreadthFirstSearch,
                '5': AStarSearch,
                '6': [Dijkstra, BellmanFord, DepthFirstSearch, BreadthFirstSearch, AStarSearch],
            }

            print("Digite una opcion:")
            print("1. Dijkstra")
            print("2. Bellman-Ford")
            print("3. Depth-First Search (DFS)")
            print("4. Breadth-First Search (BFS)")
            print("5. A Star Search")
            print("6. Todos")
            print("7. Salir")

            choice = input("Tu elección: ")

            EXIT_STRING = '7'
            if choice == EXIT_STRING:
                print("Saliendo del programa.")
                break

            grid = read_csv(full_file_path)
            start, end = find_start_end(grid)

            paths = []

            if choice in algoritmos:
                selected_algorithms = algoritmos[choice]
                if isinstance(selected_algorithms, list):
                    path_number = 4
                    for algorithm_class in selected_algorithms:
                        algorithm = algorithm_class()
                        path = maze_start(algorithm, end, grid, start)
                        paths.append((path, path_number))
                        path_number += 1
                    if choice == '6':
                        visualize_multiple_routes(grid, paths, end)
                else:
                    algorithm = selected_algorithms()
                    path = maze_start(algorithm, end, grid, start)
                    maze_visualize(grid, path, paths)

        except (ValueError, IndexError):
            print("Por favor, ingresa una opción válida.")


def maze_visualize(grid, path, paths):
    visualize_route(grid, path, 5)
    paths.append((path, 5))


def maze_start(algorithm, end, grid, start):
    path, stats = measure_performance(algorithm, "find_shortest_path", grid, start, end)
    print(f"Ruta más corta usando {algorithm.__class__.__name__}: {path}")
    save_to_csv(algorithm.__class__.__name__, path, stats)
    return path


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Se produjo un error: {e}")
