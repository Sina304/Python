from parrarel_sorting_multiprocessing import parallel_sort
import random
import time
import statistics

import matplotlib.pyplot as plt
import pandas as pd

def benchmark_and_plot():
    # zwiększone rozmiary żeby zobaczyć faktyczny wpływ równoległości
    sizes = [1000, 5000, 10000, 50000, 100000]
    process_counts = [1, 2, 4, 8]
    repetitions = 5  # ile razy powtarzamy każdy pomiar
    results = []

    for n in sizes:
        basedata = [random.randint(0, 1000000) for _ in range(n)]
        for p in process_counts:
            times = []
            for r in range(repetitions):
                data_copy = list(basedata)  # kopiujemy, żeby każdy przebieg był taki sam
                start = time.perf_counter()
                parallel_sort(data_copy, p)
                end = time.perf_counter()
                times.append(end - start)
            median_time = statistics.median(times)
            results.append({"size": n, "processes": p, "time": median_time})
            print(f"n={n}, p={p}, median_time={median_time:.6f}s (reps={repetitions})")

    df = pd.DataFrame(results)

    plt.figure(figsize=(10, 6))
    for p in process_counts:
        sub = df[df["processes"] == p].sort_values("size")
        plt.plot(sub["size"], sub["time"], marker='o', label=f"{p} processes")

    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.title("Parallel Sort Performance Benchmark (median of 5 runs)")
    plt.xscale("log")   # log scale ułatwia czytanie dla szerokiego zakresu rozmiarów
    plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == "__main__":
    benchmark_and_plot()
