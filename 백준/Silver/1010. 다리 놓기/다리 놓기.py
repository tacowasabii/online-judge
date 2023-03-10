def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(factorial(b) // (factorial(b - a) * factorial(a)))