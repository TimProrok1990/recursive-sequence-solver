def F_memo(n, d, base, memo=None):
    """
    Вычисляет n-й член последовательности с использованием мемоизации.
    
    Параметры:
    n    - искомый номер элемента (n > d)
    d    - параметр рекурсии
    base - список базовых значений
    memo - словарь для кэширования результатов (по умолчанию None)

    Сложность:
    Время: O(n * d)
    Память: O(n)
    """
    if memo is None:
        memo = {}

    if n <= d:
        return base[n - 1]
    if n in memo:
        return memo[n]

    result = 0
    for i in range(1, d + 1):
        result += F_memo(n - i, d, base, memo)
    
    memo[n] = result
    return result

if __name__ == "__main__":
    d = 3
    base = [1, 1, 2]
    n = 7

    print("=== Рекурсия с мемоизацией ===")
    print("Входные данные:")
    print("  d =", d)
    print("  base =", base)
    print("  n =", n)

    result = F_memo(n, d, base)
    print("Результат вычисления:", result)




