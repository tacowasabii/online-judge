def solution(n):
    a = 0
    b = 1
    if n == 1:
        return 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b % 1234567