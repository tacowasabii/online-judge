import sys

input = sys.stdin.readline

n = int(input())

i = 1
dic = {1: 1, 0: 0}
while i < n:
    one = 0
    zero = 0
    one += dic[0]
    zero += dic[0] + dic[1]
    dic[1] = one
    dic[0] = zero
    i += 1
ans = 0
for v in dic.values():
    ans += v
print(ans)