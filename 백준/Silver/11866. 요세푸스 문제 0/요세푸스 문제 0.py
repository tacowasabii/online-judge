from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
a = list(range(1, n+1))
ans = deque()

# 첫 번째 삭제할 원소의 인덱스
cur = k - 1

while a:
    ans.append(a[cur])
    a.pop(cur)
    if not a:
        break
    cur = (cur + k - 1) % len(a)



print("<" + ", ".join(map(str, ans)) + ">")