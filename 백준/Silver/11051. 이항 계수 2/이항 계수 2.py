def factorial(n):
    if n == 0:
        return 1
    cnt = 1
    ans = 1
    while cnt <= n:
        ans *= cnt
        cnt += 1
    return ans


a, b = map(int, input().split())
print((factorial(a) // (factorial(a - b) * factorial(b))) % 10007)