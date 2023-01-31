m = int(input())
n = int(input())
a = []
for i in range(m, n + 1):
    flag = 0
    if i == 1:
        flag = 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = 1
    if flag == 0:
        a.append(i)
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(a[0])