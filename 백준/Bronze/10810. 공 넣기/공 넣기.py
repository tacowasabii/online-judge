n, m = map(int, input().split())
a = [0 for _ in range(n + 1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j + 1):
        a[l] = k
for i in range(1, len(a)):
    print(a[i], end=' ')