import sys

input = sys.stdin.readline

n, b = input().split()
b = int(b)
ans = 0
for i in range(len(n)):
    if ord('A') <= ord(n[i]) <= ord('Z'):
        ans += b ** (len(n) - i - 1) * (ord(n[i]) - ord('A') + 10)
    else:
        ans += b ** (len(n) - i - 1) * int(n[i])
print(ans)