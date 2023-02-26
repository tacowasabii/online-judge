import sys

n, m = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
end = max(a)
start = 1

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in a:
        if i > mid:
            cnt += i - mid
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1


print(end)