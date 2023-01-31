n = int(input())
for _ in range(n):
    k = int(input()) + 2
    n = int(input())
    num = []
    for _ in range(k):
        num.append([1])
    for _ in range(n - 1):
        num[0].append(1)
    row = k
    col = n
    for i in range(1, row):
        for j in range(0, col - 1):
            num[i].append(num[i][j] + num[i - 1][j + 1])
    print(num[k - 1][n - 1])