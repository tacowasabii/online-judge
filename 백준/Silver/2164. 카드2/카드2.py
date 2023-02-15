from collections import deque

a = deque([x for x in range(1, int(input()) + 1)])

while len(a) > 1:
    a.popleft()
    tmp = a.popleft()
    a.append(tmp)

print(a[0])