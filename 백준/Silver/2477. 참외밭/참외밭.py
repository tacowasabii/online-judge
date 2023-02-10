import sys

n = int(input())
a = []
r = []
c = []
for i in range(6):
    j, k = map(int, input().split())
    a.append(k)
    if i % 2 == 0:
        r.append(k)
    else:
        c.append(k)

rmax = max(r)
cmax = max(c)
idx_r = r.index(rmax) * 2
idx_c = c.index(cmax) * 2 + 1

idx = min(idx_r, idx_c)
if max(idx_r, idx_c) == 5 and idx == 0:
    print((rmax * cmax - a[2] * a[3]) * n)
else:
    print((rmax * cmax - a[(idx + 3) % 6] * a[(idx + 4) % 6]) * n)