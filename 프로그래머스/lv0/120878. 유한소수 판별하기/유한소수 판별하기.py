def solution(a, b):
    c = 0
    prime = []
    num = min(a, b)
    for i in range(num, 0, -1):
        if a % i == 0 and b % i == 0:
            c = b / i
            break
    d = 2
    while d <= c:
        if c % d == 0:
            prime.append(d)
            c = c / d
        else:
            d = d + 1

    prime = set(prime)
    prime.discard(2)
    prime.discard(5)
    
    if len(prime) > 0:
        return 2
    else:
        return 1