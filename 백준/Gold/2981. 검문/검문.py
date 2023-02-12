import math

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()
b = [a[i + 1] - a[i] for i in range(n - 1)]

gcd = max(b)
for i in b:
    gcd = math.gcd(i, gcd)

ans = []
for i in range(1, int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        ans.append(i)
        ans.append(gcd // i)
ans = list(set(ans))
ans.sort()
ans = ans[1:]
print(*ans)