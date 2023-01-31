n = int(input())
for _ in range(n):
    h, w, n = map(int, input().split())
    if n % h == 0:
        floor = str(h)
    else:
        floor = str(n % h)
    num = str(((n - 1) // h + 1)).zfill(2)
    print(floor + num)