import sys

k, n = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(sys.stdin.readline()))

start = 1
end = max(a)
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in a:
        cnt += i // mid
    if cnt < n:
        end = mid - 1
    elif cnt >= n:
        start = mid + 1
print(end)