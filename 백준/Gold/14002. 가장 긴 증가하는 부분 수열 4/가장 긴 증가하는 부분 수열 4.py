import bisect

n = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]
idx_list = [0]  # idx_list[i]: LIS[i]가 A에서의 인덱스
for i in range(1, n):
    if A[i] > LIS[-1]:
        LIS.append(A[i])
        idx_list.append(len(LIS) - 1)
    else:
        idx = bisect.bisect_left(LIS, A[i])
        LIS[idx] = A[i]
        idx_list.append(idx)

ans = []
last_idx = len(LIS) - 1
for i in range(n-1, -1, -1):
    if idx_list[i] == last_idx:
        ans.append(A[i])
        last_idx -= 1

print(len(ans))
print(*reversed(ans))