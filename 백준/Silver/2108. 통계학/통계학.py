import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()
count = {}
for i in num:
    count[i] = count.get(i, 0) + 1
max_count = max([v for k, v in count.items()])
a = [k for k, v in count.items() if v == max_count]

print(round(sum(num) / len(num)))
print(num[n // 2])
print(a[0] if len(a) == 1 else a[1])
print(max(num) - min(num))