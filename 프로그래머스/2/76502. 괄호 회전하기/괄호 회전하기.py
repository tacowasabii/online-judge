def isPossible(s):
    stack = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        elif stack:
            if i == ")" and stack[-1] == "(" or i == "}" and stack[-1] == "{" or i == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False
        else:
            return False
    return len(stack) == 0

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if isPossible(s[i:] + s[:i]):
            answer += 1
    return answer