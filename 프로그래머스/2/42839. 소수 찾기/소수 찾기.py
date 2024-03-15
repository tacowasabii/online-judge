from itertools import permutations

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = list(numbers)
    n = []
    for i in range(len(nums)):
        n += list(permutations(nums, i+1))
    nums = []
    for i in n:
        tmp = ''
        for j in i:
            tmp += j
        tmp = int(tmp)
        if tmp not in nums and tmp != 1 and tmp != 0:
            nums.append(tmp)
    for i in nums:
        if isPrime(i):
            answer += 1
    return answer