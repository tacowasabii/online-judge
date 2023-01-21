def solution(s):
    return ''.join(sorted(s, reverse=True, key=ord))
