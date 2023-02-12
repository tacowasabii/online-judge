a = int(input())
b = int(input())
c = int(input())
n = str(a * b * c)
dic = {}
for i in n:
    dic[int(i)] = dic.get(int(i), 0) + 1
cnt = 0
while cnt < 10:
    if cnt in dic:
        print(dic[cnt])
    else:
        print(0)
    cnt += 1