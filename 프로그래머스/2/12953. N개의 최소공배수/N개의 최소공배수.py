def lcm(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return a * b // gcd

def solution(arr):
    num = arr[0]
    
    for i in arr:
        num = lcm(num, i)
        
    return num