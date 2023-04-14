import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    num = [n]
    while len(num) > 0:
        tmp = []
        for i in num:
            if i - 1 >= 0:
                tmp.append(i - 1)
            if i - 2 >= 0:
                tmp.append(i - 2)
            if i - 3 >= 0:
                tmp.append(i - 3)
        num = []
        for i in tmp:
            if i == 0:
                cnt += 1
            else:
                num.append(i)
    print(cnt)