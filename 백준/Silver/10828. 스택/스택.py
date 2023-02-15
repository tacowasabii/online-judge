import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if not stack:
            print(-1)
        else:
            tmp = stack.pop()
            print(tmp)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])