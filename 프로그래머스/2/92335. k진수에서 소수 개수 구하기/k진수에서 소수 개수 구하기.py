def TentoK(n, k):
    tmp = ''
    while n:
        tmp += str(n % k)
        n //= k
    return tmp[::-1]

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    toK = TentoK(n,k)
    tmp = toK.split("0")
    cnt = 0
    for i in tmp:
        if i !='' and isPrime(int(i)):
            cnt += 1
    return cnt