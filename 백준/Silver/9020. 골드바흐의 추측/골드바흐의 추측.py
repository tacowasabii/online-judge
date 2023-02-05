def isPrime(n):
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


count = int(input())
for _ in range(count):
    n = int(input())
    a = n // 2
    b = round(n // 2)
    while True:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        a -= 1
        b += 1
