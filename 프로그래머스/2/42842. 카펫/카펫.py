def solution(brown, yellow):
    num = (brown - 4) // 2
    for i in range(1, num ):
        if i * (num - i) == yellow:
            return [num - i + 2, i + 2]