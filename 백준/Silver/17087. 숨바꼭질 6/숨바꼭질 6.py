import sys
from math import gcd

input = sys.stdin.readline

n, s = map(int, input().split())
p = list(map(int, input().split()))
ans = abs(s - p[0])
for i in range(1, len(p)):
    ans = gcd(ans, abs(p[i] - s))
print(ans)