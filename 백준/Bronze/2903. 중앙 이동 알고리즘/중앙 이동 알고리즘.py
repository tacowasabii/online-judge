import sys

input = sys.stdin.readline

n = int(input()) - 1
print((2 ** (n + 1) + 1) ** 2)