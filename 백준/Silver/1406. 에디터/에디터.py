from collections import deque
import sys

a = deque(input())
b = deque()
n = int(input())
for _ in range(n):
    order = sys.stdin.readline().strip()
    if order[0] == 'P':
        a.append(order[-1])
    elif order[0] == 'L':
        if len(a) > 0:
            tmp = a.pop()
            b.appendleft(tmp)
    elif order[0] == 'B':
        if len(a) > 0:
            a.pop()
    else:
        if len(b) > 0:
            tmp = b.popleft()
            a.append(tmp)
print(''.join(a + b))