n = input()
dic = {}
nlist = list(input().split())
for i in nlist:
    dic[i] = dic.get(i, 0) + 1

m = input()
mlist = list(input().split())
for i in mlist:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')