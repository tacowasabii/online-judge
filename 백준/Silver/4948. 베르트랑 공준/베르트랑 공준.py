def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, int(n ** 0.5) + 1):
        if i in num:
            num -= set(range(i * i, n + 1, i))
    return num


while True:
    n = int(input())
    if n == 0:
        break
    a = solution(n * 2) - solution(n)
    print(len(a))