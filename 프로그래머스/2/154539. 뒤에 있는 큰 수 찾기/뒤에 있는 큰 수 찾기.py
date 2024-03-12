def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i, v in enumerate(numbers):
        while stack and v > numbers[stack[-1]]:
            idx = stack.pop()
            answer[idx] = v
        stack.append(i)
    return answer