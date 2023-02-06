import sys

n = int(input())
info = []
for i in range(n):
    info.append(list(sys.stdin.readline().split()))
    info[-1][0] = int(info[-1][0])

info.sort(key=lambda x: x[0])
for i in info:
    print(i[0], i[1])