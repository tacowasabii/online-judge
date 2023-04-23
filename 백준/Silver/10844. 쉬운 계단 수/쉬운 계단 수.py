import sys

input = sys.stdin.readline
n = int(input())

dic = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
cnt = n
while cnt > 1:
    tmp = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for k in dic.keys():
        if k == 0:
            tmp[1] += dic[0]
        elif k == 9:
            tmp[8] += dic[9]
        else:
            tmp[k + 1] += dic[k]
            tmp[k - 1] += dic[k]
    dic = tmp
    cnt -= 1

print(sum(dic.values()) % 1000000000)