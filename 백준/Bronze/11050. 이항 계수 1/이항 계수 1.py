def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


a, b = map(int, input().split())
print(factorial(a) // (factorial(a - b) * factorial(b)))