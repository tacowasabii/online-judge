def solution(numbers):
    result = [-1] * len(numbers)
    stack = []
    for i, v in enumerate(numbers):
        while stack and stack[-1][1] < v:
            tmp = stack.pop()
            result[tmp[0]] = v
        stack.append((i, v))
    return result