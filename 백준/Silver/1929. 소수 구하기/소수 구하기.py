def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, int(n ** 0.5) + 1):
        if i in num:
            num -= set(range(i * i, n + 1, i))
    return num


m, n = map(int, input().split())
a = solution(n) - solution(m - 1)
for i in sorted(list(a)):
    print(i)