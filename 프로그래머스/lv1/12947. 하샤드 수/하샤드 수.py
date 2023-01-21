def solution(x):
    num = sum(map(int, list(str(x))))
    return True if x % num == 0 else False