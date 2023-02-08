n, m = map(int, input().split())
list = []
for _ in range(n):
    list.append(input())

minn = 64

for a in range(n - 7):
    for b in range(m - 7):
        count = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if list[i][j] != 'B':
                            count += 1
                    else:
                        if list[i][j] != 'W':
                            count += 1
                else:
                    if j % 2 == 0:
                        if list[i][j] != 'W':
                            count += 1
                    else:
                        if list[i][j] != 'B':
                            count += 1
        minn = min(count, minn)

for a in range(n - 7):
    for b in range(m - 7):
        count = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if list[i][j] != 'W':
                            count += 1
                    else:
                        if list[i][j] != 'B':
                            count += 1
                else:
                    if j % 2 == 0:
                        if list[i][j] != 'B':
                            count += 1
                    else:
                        if list[i][j] != 'W':
                            count += 1
        minn = min(count, minn)

print(minn)