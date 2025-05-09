def F_naive(n, d, base):
    """
    Вычисляет n-й член последовательности наивной рекурсией.
    
    Параметры:
    n    - искомый номер элемента (n > d)
    d    - параметр рекурсии (количество суммируемых предыдущих элементов)
    base - список базовых значений [F(1), F(2), ..., F(d)]

    Сложность:
    Время: экспоненциальное ~ O(d^(n-d))
    Память: O(n) (глубина рекурсии)
    """
    if n <= d:
        return base[n - 1]  # базовые случаи

    result = 0
    for i in range(1, d + 1):
        result += F_naive(n - i, d, base)
    return result

if __name__ == "__main__":
    d = 3
    base = [1, 1, 2]
    n = 7

    print("=== Наивная рекурсия ===")
    print("Входные данные:")
    print("  d =", d)
    print("  base =", base)
    print("  n =", n)

    result = F_naive(n, d, base)
    print("Результат вычисления:", result)

