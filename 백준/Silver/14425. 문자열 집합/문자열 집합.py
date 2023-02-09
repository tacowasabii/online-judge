import sys

n, m = map(int, input().split())
a = set()
b = []
for _ in range(n):
    a.add(sys.stdin.readline().strip())
for _ in range(m):
    b.append(sys.stdin.readline().strip())

count = 0
for i in b:
    if i in a:
        count += 1
print(count)