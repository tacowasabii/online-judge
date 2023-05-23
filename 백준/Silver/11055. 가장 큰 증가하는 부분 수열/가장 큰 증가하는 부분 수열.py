N = int(input())
A = list(map(int, input().split()))
DP = A.copy()

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j] + A[i])

print(max(DP))