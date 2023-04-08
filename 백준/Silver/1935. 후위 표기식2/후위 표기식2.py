import sys
from collections import deque

n = int(input())
m = input()
stack = []
num = {}
alp = 65
for _ in range(n):
    num[chr(alp)] = int(sys.stdin.readline())
    alp += 1
for i in m:
    if i == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif i == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif i == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif i == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
    else:
        stack.append(num[i])
result = stack[0]
print(f'{result:.2f}')