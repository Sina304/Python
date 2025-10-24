import multiprocessing as mp
from heapq import merge

def parallel_sort(data, num_workers):
    """
    Sortuje listę data równolegle przy użyciu num_workers procesów.
    Jeśli num_workers <= 1, używa wbudowanego sorted().
    Zwraca posortowaną listę.
    """
    if num_workers <= 1:
        return sorted(data)

    n = len(data)
    # chunk_size tak, żeby pokryć całą listę
    chunk_size = max(1, (n + num_workers - 1) // num_workers)
    chunks = [data[i:i + chunk_size] for i in range(0, n, chunk_size)]

    # Pool tylko wewnątrz funkcji (bez globalnych efektów ubocznych)
    ctx = mp.get_context("spawn")  # bezpieczne podejście cross-platform
    with ctx.Pool(processes=min(num_workers, len(chunks))) as pool:
        sorted_chunks = pool.map(sorted, chunks)

    # wieloetapowe łączenie par (log k etapów), używamy heapq.merge
    while len(sorted_chunks) > 1:
        merged = []
        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                # merge zwraca iterator, zamieniamy na listę aby zachować dane
                merged.append(list(merge(sorted_chunks[i], sorted_chunks[i + 1])))
            else:
                merged.append(sorted_chunks[i])
        sorted_chunks = merged

    return sorted_chunks[0] if sorted_chunks else []