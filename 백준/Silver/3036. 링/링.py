import math

n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    gcd = math.gcd(a[0], a[i])
    print(str(a[0] // gcd) + '/' + str(a[i] // gcd))