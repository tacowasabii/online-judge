n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    temp = list(map(int, input().split()))
    a.append(temp)
for _ in range(n):
    temp = list(map(int, input().split()))
    b.append(temp)
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
for i in range(n):
    for j in a[i]:
        print(j, end=' ')
    print()