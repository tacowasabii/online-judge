n = int(input())
for _ in range(n):
    a = list(input().split())
    for i in a:
        print(i[::-1], end=' ')