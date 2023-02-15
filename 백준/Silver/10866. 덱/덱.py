import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push_back':
        stack.append(order[1])
    elif order[0] == 'push_front':
        stack.appendleft(order[1])
    elif order[0] == 'pop_front':
        if not stack:
            print(-1)
        else:
            tmp = stack.popleft()
            print(tmp)
    elif order[0] == 'pop_back':
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
    elif order[0] == 'front':
        if not stack:
            print(-1)
        else:
            print(stack[0])
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])