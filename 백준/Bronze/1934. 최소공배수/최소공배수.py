n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    c, d = a, b
    while a != 0:
        tmp = a
        a = b % a
        b = tmp
        if a == 0:
            print(c * d // b)