import time

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
    main = arr[0]
    less = [x for x in arr[1:] if x <  main]
    more = [x for x in arr[1:] if x >=  main]
    return quick_sort(less) + [main] + quick_sort(more)


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

a = [1, 5, 6, 234, 43, 31, 23, 40, 51, 60]
b = [4545435435341, 5, 6, 234, 45463, 31, 24563, 45460, 54561, 646560]
c = [4545, 3455, 645, 234, 45463, 31, 24563, 45460, 54561, 646560]

print(bubble_sort(a))
print(quick_sort(b))
print(radix_sort(c))