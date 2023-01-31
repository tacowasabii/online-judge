n = int(input())
a = list(map(int, input().split()))
count = 0
for i in a:
    flag = 0
    if i == 1:
        flag = 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = 1
    if flag == 0:
        count += 1
print(count)