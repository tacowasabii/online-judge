import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
numss = sorted(list(set(nums)))
dic = {numss[i]: i for i in range(len(numss))}

for i in nums:
    print(dic[i], end=' ')