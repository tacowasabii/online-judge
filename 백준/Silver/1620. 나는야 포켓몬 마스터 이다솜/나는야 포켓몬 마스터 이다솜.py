import sys

n, m = map(int, input().split())
name_dic = {}
num_dic = {}
for i in range(n):
    tmp = sys.stdin.readline().strip()
    name_dic[tmp] = i + 1
    num_dic[i + 1] = tmp
for _ in range(m):
    a = sys.stdin.readline().strip()
    if a.isalpha():
        print(name_dic[a])
    else:
        print(num_dic[int(a)])