import tracemalloc
import psutil
import time


def measure_performance(algorithm, method_name, maze, start, end):
    tracemalloc.start()

    initial_memory = psutil.Process().memory_info().rss / 1024  # in KB

    start_time = time.time()

    path = getattr(algorithm, method_name)(maze, start, end)

    end_time = time.time()

    # in seconds with 4 decimals
    elapsed_time = round(end_time - start_time, 4)

    final_memory = psutil.Process().memory_info().rss / 1024  # in KB

    memory_increment = final_memory - initial_memory  # in KB

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()


    print("\nTiempo transcurrido:", elapsed_time, "segundos")
    print("Incremento de memoria:", memory_increment, "KB")
    print("Pico de memoria:", peak / 1024, "KB")

    results = {
        'time': elapsed_time,
        'memory_increment': memory_increment,
        'peak_memory': peak / 1024 # in KB
    }

    return path, results
