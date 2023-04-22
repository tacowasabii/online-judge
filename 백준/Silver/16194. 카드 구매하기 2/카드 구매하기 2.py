import sys

input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
ans = 0
dp = [sys.maxsize] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        tmp = []
        dp[i] = min(dp[i], dp[i - j] + p[j - 1])
print(dp[n])