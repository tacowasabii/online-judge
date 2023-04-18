import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1]
for i in range(1, len(a)):
    tmp = 0
    for j in range(i):
        if a[j] < a[i]:
            tmp = max(tmp, dp[j])
    dp.append(tmp + 1)
print(max(dp))
