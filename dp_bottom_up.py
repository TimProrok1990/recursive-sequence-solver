def F_bottom_up(n, d, base):
    """
    Вычисляет n-й член последовательности итеративно (Bottom-Up).
    
    Параметры:
    n    - искомый номер элемента (n > d)
    d    - параметр рекурсии
    base - список базовых значений

    Сложность:
    Время: O(n * d)
    Память: O(n)
    """
    dp = [0] * n  # инициализируем массив для значений от 1 до n

    # Заполнение базовых случаев
    for i in range(d):
        dp[i] = base[i]

    # Вычисление последующих значений
    for i in range(d, n):
        dp[i] = sum(dp[i - d:i])

    return dp[n - 1]

if __name__ == "__main__":
    d = 3
    base = [1, 1, 2]
    n = 7

    print("=== Итеративный DP (Bottom-Up) ===")
    print("Входные данные:")
    print("  d =", d)
    print("  base =", base)
    print("  n =", n)

    result = F_bottom_up(n, d, base)
    print("Результат вычисления:", result)


