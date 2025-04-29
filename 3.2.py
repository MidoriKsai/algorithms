import time
import random

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            positions.append(i)
    return positions


def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    positions = []
    shift = 0
    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            positions.append(shift)
            shift += (m - bad_char.get(text[shift + m], -1)) if shift + m < n else 1
        else:
            shift += max(1, j - bad_char.get(text[shift + j], -1))
    return positions


def rabin_karp_search(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)
    positions = []
    if m == 0 or m > n:
        return positions

    h = pow(d, m - 1, q)
    p_hash = 0
    t_hash = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                positions.append(i)
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q
    return positions


def generate_test_case(text_len=1000, pattern_len=10):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    text = ''.join(random.choice(alphabet) for _ in range(text_len))

    start_pos = random.randint(0, text_len - pattern_len)
    pattern = text[start_pos:start_pos + pattern_len]

    return text, pattern


def measure_search(search_func, text, pattern, iterations=10):
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        search_func(text, pattern)
        total_time += time.time() - start_time
    return total_time / iterations


text, pattern = generate_test_case(10000, 10)

print(f"Длина текста: {len(text)}, длина паттерна: {len(pattern)}")
print(f"  Наивный алгоритм: {measure_search(naive_search, text, pattern):.6f} сек")
print(f"  Бойера-Мура: {measure_search(boyer_moore_search, text, pattern):.6f} сек")
print(f"  Рабина-Карпа: {measure_search(rabin_karp_search, text, pattern):.6f} сек")