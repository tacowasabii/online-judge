import sys

n, m = map(int, input().split())
a = set()
b = set()

for _ in range(n):
    a.add(sys.stdin.readline().strip())
for _ in range(m):
    b.add(sys.stdin.readline().strip())
tmp = list(a & b)
tmp.sort()
print(len(tmp))
for i in tmp:
    print(i)