from itertools import combinations as cb

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in list(cb(nums, 3)):
        if isPrime(sum(i)):
            answer += 1
    return answer