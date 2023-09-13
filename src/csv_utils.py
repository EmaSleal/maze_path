"""
Este módulo contiene utilidades para leer una cuadrícula desde un archivo CSV,
"""
import os
import csv


directorio_actual = os.path.dirname(__file__)
BASE_PATH = os.path.dirname(directorio_actual)
FILE_PATH = "data/ultra_route.csv"
SAVE_PATH = "docs/"


def read_csv(file_path):
    import logging
    """Lee una cuadrícula desde un archivo CSV y la devuelve como una lista de listas."""
    grid = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                grid.append([int(item) for item in row])
                import logging

    except (FileNotFoundError, PermissionError) as e:
        logging.error(f"Error: {e}")
        raise e
    return grid


def save_to_csv(algorithm_name, path, stats):
    unique_id = 1
    file_name1 = f"ruta_{algorithm_name}_laberinto_{unique_id}.csv"
    full_save_path1 = os.path.join(BASE_PATH, SAVE_PATH, file_name1)

    file_name2 = f"estadisticas_{algorithm_name}_laberinto_{unique_id}.csv"
    full_save_path2 = os.path.join(BASE_PATH, SAVE_PATH, file_name2)

    with open(full_save_path1, mode='w', newline='') as file:
        writer = csv.writer(file)

        data = [
            [f"Resultados y Estadisticas con el algoritmo: {algorithm_name}"],
            ["La ruta mas corta es:"],
            path,
        ]
        writer.writerows(data)

    with open(full_save_path2, mode='w', newline='') as file:
        writer = csv.writer(file)

        data = [
            ["Las estadisticas son:"],
            ["Tiempo (s)", "Incremento de memoria (KB)", "Memoria maxima (KB)"],
            [stats['time'], stats['memory_increment'], stats['peak_memory']]
        ]
        writer.writerows(data)