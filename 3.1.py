import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    min_num = min(arr)
    if min_num < 0:
        shift = -min_num
        arr = [num + shift for num in arr]
    else:
        shift = 0
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    if shift > 0:
        arr = [num - shift for num in arr]
    return arr

def measure_time(sort_func, arr, iterations=10):
    total_time = 0
    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_func(arr_copy)
        total_time += time.time() - start_time
    return total_time / iterations

large_array = [random.randint(0, 10000) for _ in range(1000)]

bubble_time = measure_time(bubble_sort, large_array)
quick_time = measure_time(quick_sort, large_array)
radix_time = measure_time(radix_sort, large_array)

print("Большой массив (1000 элементов):")
print(f"  Пузырьковая сортировка: {bubble_time:.6f} сек")
print(f"  Быстрая сортировка: {quick_time:.6f} сек")
print(f"  Поразрядная сортировка: {radix_time:.6f} сек")