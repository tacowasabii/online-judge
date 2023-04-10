import sys

input = sys.stdin.readline

prime = [True for _ in range(1000001)]

for i in range(2, 1001):
    if prime[i]:
        for j in range(i * 2, 1000001, i):
            prime[j] = False
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n - i]:
            cnt += 1
    print(cnt)