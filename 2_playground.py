def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)  # Output: Sorted array: [3, 9, 10, 27, 38, 43, 82]

arr2 = [5, 2, 9, 1, 5, 6]
sorted_arr2 = merge_sort(arr2)
print("Sorted array:", sorted_arr2)  # Output: Sorted array: [1, 2, 5, 5, 6, 9]

sorted_all=merge(sorted_arr, sorted_arr2)
print("Sorted combined array:", sorted_all)  # Output: Sorted combined array: [1, 2, 3, 5, 5, 6, 9, 10, 27, 38, 43, 82]
