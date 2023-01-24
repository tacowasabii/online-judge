n = int(input())
a = list(map(int, input().split()))
b = int(input())
count = 0
for i in range(n):
    if a[i] == b:
        count += 1
print(count)