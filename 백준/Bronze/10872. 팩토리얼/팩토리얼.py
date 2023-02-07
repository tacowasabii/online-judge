n = int(input())

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

ans = fact(n)
print(ans)