import sys
from math import factorial

input = sys.stdin.readline

n = int(input())

def combination(a,b):
    return factorial(a)//(factorial(b)*factorial(a-b))

cnt = 0
if n % 2 == 0:
    for i in range(0, n + 1, 2):
        cnt += combination((n + i) // 2, i)*2**((n-i)//2)
    print(cnt % 10007)
else:
    for i in range(1, n + 1, 2):
        cnt += combination((n + i) // 2, i)*2**((n-i)//2)
    print(cnt % 10007)