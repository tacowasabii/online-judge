def solution(n):
    if n % 2 == 0:
        a = n // 2
        return a * (a + 1) * (2 * a + 1) // 6 * 4
    else:
        return (1 + n) * (n // 2 + 1) // 2