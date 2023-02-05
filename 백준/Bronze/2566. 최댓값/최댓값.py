a = []
for _ in range(9):
    temp = list(map(int, input().split()))
    a.append(temp)

num = 0
idx = [0, 0]
for r_idx, rv in enumerate(a):
    for c_idx, cv in enumerate(rv):
        if a[r_idx][c_idx] >= num:
            num = a[r_idx][c_idx]
            idx[0] = r_idx + 1
            idx[1] = c_idx + 1

print(num)
print(idx[0], idx[1])