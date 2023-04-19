import sys

input = sys.stdin.readline

a = []
cnt = 0
for _ in range(5):
    tmp = input().strip()
    a.append(tmp)
    cnt = max(cnt, len(tmp))
ans = ''
for i in range(cnt):
    for j in range(5):
        try:
            ans += a[j][i]
        except:
            continue
print(ans)