import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (n + 1)
dp[0] = 1
for _ in range(k):
    tmp = [0] * (n + 1)
    for i in range(n + 1):
        for j in range(i + 1):
            tmp[i] += dp[j]
    dp = tmp
print(dp[n] % 1000000000)