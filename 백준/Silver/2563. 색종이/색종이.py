a = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            a[i][j] = 1

count = 0
for i in a:
    count += i.count(1)

print(count)