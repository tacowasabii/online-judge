n = int(input())
list = []
for _ in range(n):
    w, h = map(int, input().split())
    list.append([w, h])

num = []
for i in list:
    count = 0
    for j in list:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    num.append(count + 1)

for i in num:
    print(i, end=' ')