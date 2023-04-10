import sys
from math import ceil

input = sys.stdin.readline

n = int(input())

ans = ''
flag = True
if n == 0:
    print(0)
    flag = False

while flag:
    if n == 1:
        ans = '1' + ans
        break
    ans = str(abs(n % -2)) + ans
    n = ceil(n / -2)

print(ans)