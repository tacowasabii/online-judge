import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
num = [n]

while True:
    if n == 1:
        print(0)
        break
    tmp = []
    cnt += 1
    for i in num:
        if i % 3 == 0:
            tmp.append(i // 3)
        if i % 2 == 0:
            tmp.append(i // 2)
        tmp.append(i - 1)
    if 1 in tmp:
        print(cnt)
        break
    num = tmp
    tmp = []