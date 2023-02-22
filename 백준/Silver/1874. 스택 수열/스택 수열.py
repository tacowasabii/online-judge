import sys

n = int(input())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

stack = ['']

idx = 0
num = 1
ans = []
flag = 0
while idx < n:
    if stack[-1] == a[idx]:
        idx += 1
        stack.pop()
        ans.append('-')
    elif num <= a[idx]:
        stack.append(num)
        num += 1
        ans.append('+')
    elif stack[-1] != a[idx]:
        print('NO')
        flag = 1
        break
if flag == 0:
    for i in ans:
        print(i)