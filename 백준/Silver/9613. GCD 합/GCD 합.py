import sys
from math import gcd

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    gcds = []
    a = list(map(int, input().split()))
    num = a[0]
    b = a[1:]
    for i in range(num - 1):
        for j in range(i + 1, num):
            gcds.append(gcd(b[i], b[j]))
    print(sum(gcds))