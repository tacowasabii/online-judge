import sys

n = int(input())
for _ in range(n):
    m = int(sys.stdin.readline())
    q = m // 25
    d = (m - q * 25) // 10
    n = (m - q * 25 - d * 10) // 5
    p = m - q * 25 - d * 10 - n * 5
    print(q, d, n, p)