import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    a = []
    for i in range(1, n):
        if n % i == 0:
            a.append(i)
    if sum(a) == n:
        print(n, '= ', end='')
        for i in range(len(a) - 1):
            print(a[i], '+ ', end='')
        print(a[-1])
    else:
        print(f'{n} is NOT perfect.')