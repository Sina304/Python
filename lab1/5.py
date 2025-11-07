import random

# Generowanie liczb
N = 10
numbers = [random.randint(1, 100) for _ in range(N)]
print("Przed sortowaniem:", numbers)

# Sortowanie bąbelkowe "https://pl.wikipedia.org/wiki/Sortowanie_b%C4%85belkowe"
def sort_1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

# Sortowanie przez wstawianie "https://pl.wikipedia.org/wiki/Sortowanie_przez_wstawianie"
def sort_2(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Testowanie
sorted_1 = sort_1(numbers.copy())
sorted_2 = sort_2(numbers.copy())
verified = sorted(numbers)

print("Sortowanie (wersja 1):", sorted_1)
print("Sortowanie (wersja 2):", sorted_2)
print("Weryfikacja (wbudowane sortowanie):", verified)
print("Czy wyniki się zgadzają?", sorted_1 == verified == sorted_2)