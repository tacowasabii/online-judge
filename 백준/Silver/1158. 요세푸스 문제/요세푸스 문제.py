n, k = map(int, input().split())
ans = []
a = [x + 1 for x in range(n)]
count = n
idx = 0
for _ in range(n):
    idx = (idx + k - 1) % count
    count -= 1
    tmp = a.pop(idx)
    ans.append(tmp)
print('<', end='')
for i in range(len(ans) - 1):
    print(ans[i], end=', ')
print(ans[-1], end='')
print('>')