def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def tenToK(n, k):
    tmp = []
    while n > 0:
        tmp.append(str(n % k))
        n //= k
    return ''.join(tmp[::-1])

def solution(n, k):
    ans = 0
    nums = list(map(int, filter(None, tenToK(n, k).split("0"))))

    for i in nums:
        if isPrime(i):
            ans += 1
    
    return ans
    