n = int(input())
for _ in range(n):
    a = []
    n, s = input().split()
    for i in s:
        a.append(i * int(n))
    print(''.join(a))