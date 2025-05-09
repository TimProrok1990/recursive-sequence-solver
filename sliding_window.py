def F_sliding_window(n, d, base):
    """
    Вычисляет n-й член последовательности с использованием скользящего окна.

    Параметры:
    n    - искомый номер элемента (n > d)
    d    - параметр рекурсии
    base - список базовых значений

    Сложность:
    Время: O(n)
    Память: O(d)
    """
    window = base.copy()
    current_sum = sum(window)

    if n <= d:
        return window[n - 1]

    for _ in range(d, n):
        next_value = current_sum
        current_sum = current_sum - window.pop(0) + next_value
        window.append(next_value)

    return window[-1]

if __name__ == "__main__":
    d = 3
    base = [1, 1, 2]
    n = 7

    print("=== Скользящее окно ===")
    print("Входные данные:")
    print("  d =", d)
    print("  base =", base)
    print("  n =", n)

    result = F_sliding_window(n, d, base)
    print("Результат вычисления:", result)



