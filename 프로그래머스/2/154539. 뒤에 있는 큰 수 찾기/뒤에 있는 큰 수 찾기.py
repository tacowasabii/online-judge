def solution(numbers):
    result = [-1] * len(numbers)
    
    stack = []
    for i, v in enumerate(numbers):
        while stack and numbers[stack[-1]] < v:
            idx = stack.pop()
            result[idx] = v
        stack.append(i)
    return result