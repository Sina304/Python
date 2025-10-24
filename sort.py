from multiprocessing import Pool, cpu_count
import heapq
import math

def parallel_sort(data, x_procs=None):
    #data = [random.randint(0, 1000000) for _ in range(n)]
    #print(f"Number of CPU cores: {n_cores}")

    chunk_size = math.ceil(len(data) / x_procs)
    chunks = [data[i:(i+chunk_size)] for i in range(0, len(data), chunk_size)]
    #print(f"data length: {len(data)}")
    #print(f"Liczba fragmentów: {len(chunks)}")

    with Pool(processes=x_procs) as pool:
        sorted_chunks = pool.map(sorted, chunks)

    sorted_data = list(heapq.merge(*sorted_chunks))
    
    return (sorted_data)


# Example usage:
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    sorted_data = parallel_sort(data, 1)
    #print("Sorted data:", sorted_data)
    print("Ilość rdzeni", cpu_count())