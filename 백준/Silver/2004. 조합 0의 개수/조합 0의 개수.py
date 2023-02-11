n, m = map(int, input().split())

def count(n, k):
    cnt = 0
    while n != 0:
        n //= k
        cnt += n
    return cnt


print(min(count(n, 2) - count(n - m, 2) - count(m, 2), count(n, 5) - count(n - m, 5) - count(m, 5)))