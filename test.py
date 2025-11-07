import random
import time
from sort import parallel_sort
import matplotlib.pyplot as plt

results = {}

def test_parallel_sort(n, x_procs):
    # generujemy dane
    data = [random.randint(0, 1_000_000_000_000) for _ in range(n)]
    
    start = time.perf_counter()
    sorted_data = parallel_sort(data, x_procs)
    end = time.perf_counter()
    elapsed = end - start
    
    print(f"Rozmiar danych: {n}, ilość procesów: {x_procs}, czas sortowania: {elapsed:.6f} s")

    if n not in results:
        results[n] = []
    results[n].append((x_procs, elapsed))

if __name__ == "__main__":
    test_sizes = [20_000_000, 100]
    proc_counts = [1, 2, 4, 8, 16]

    for n in test_sizes:
        for p in proc_counts:
            test_parallel_sort(n, p)

    # WYKRES
    for n in results:
        results[n].sort(key=lambda x: x[0])  # sortujemy wg liczby procesów
        x = [p for p, _ in results[n]]
        y = [t for _, t in results[n]]
        plt.plot(x, y, marker="o", label=f"n={n}")

    plt.xlabel("Liczba procesów")
    plt.ylabel("Czas sortowania [s]")
    plt.title("Wydajność równoległego sortowania multiprocessing")
    plt.grid(True)
    plt.legend()
    plt.show()
