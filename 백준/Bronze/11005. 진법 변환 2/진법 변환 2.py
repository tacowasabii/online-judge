import sys

input = sys.stdin.readline

n, b = map(int, input().split())
ans = ''
while (n // b) >= 1:
    r = n % b
    if r < 10:
        ans = str(r) + ans
    else:
        ans = chr(r + ord('A') - 10) + ans
    n = n // b
if n < 10:
    ans = str(n) + ans
else:
    ans = chr(n + ord('A') - 10) + ans

print(ans)