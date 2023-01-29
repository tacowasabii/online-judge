def self(n):
    return n + sum(list(map(int, str(n))))

a = []
i = 1
while i <= 10000:
    tmp = self(i)
    if tmp <= 10000 and tmp not in a:
        a.append(tmp)
    i += 1

for j in range(1, 10001):
    if j not in a:
        print(j)