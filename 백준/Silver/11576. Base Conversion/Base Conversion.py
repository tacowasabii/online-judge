import sys

input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))
tmp = 0
for i in range(len(A)):
    tmp += a ** (len(A) - i - 1) * A[i]

ans = ''
while tmp // b > 0:
    ans = ' ' + str(tmp % b) + ans
    tmp //= b
    
if tmp > 0:
    ans = str(tmp) + ans
print(ans)