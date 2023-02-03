from math import gcd


def solution(arr):
    a = arr[0]
    for i in range(1, len(arr)):
        a = a * arr[i] // gcd(a, arr[i])
    return a