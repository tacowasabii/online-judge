n = int(input())
for _ in range(n):
    count = 0
    a = list(map(int, input().split()))
    avg = sum(a[1:]) / a[0]
    for i in range(1, len(a)):
        if a[i] > avg:
            count += 1
    print(format(round(count / a[0] * 100, 3), ".3f") + "%")