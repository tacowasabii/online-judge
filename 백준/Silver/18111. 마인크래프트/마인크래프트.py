import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(n)]

time = sys.maxsize
height = 0
for i in range(257):
    t = 0
    cnt = 0
    for j in block:
        for k in j:
            cnt += k - i
            if k > i:
                t += 2 * (k-i)
            elif k < i:
                t += 1 * (i-k)
    if cnt + b >= 0 and t <= time and i >= height:
        time = t
        height = i
print(time, height)
