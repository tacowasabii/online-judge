import bisect
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

LIS = [a[0]]

for i in range(1, n):
    if a[i] > LIS[-1]:
        LIS.append(a[i])
    else:
        idx = bisect.bisect_left(LIS, a[i])
        LIS[idx] = a[i]

print(len(LIS))