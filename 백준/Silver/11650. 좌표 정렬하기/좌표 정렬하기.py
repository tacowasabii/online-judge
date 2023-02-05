n = int(input())
num = []
for _ in range(n):
    num.append(list(map(int, input().split())))

num.sort(key=lambda x: (x[0], x[1]))
for i in num:
    print(i[0], i[1])