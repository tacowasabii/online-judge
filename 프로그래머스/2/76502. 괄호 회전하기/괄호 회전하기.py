def solution(s):
    answer = 0
    for _ in range(len(s)):
        stack = []
        flag = 0
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    flag = 1
                else:
                    if (i == ']' and stack[-1] == '[') or  (i == ')' and stack[-1] == '(') or  (i == '}' and stack[-1] == '{'):
                        stack.pop()
                        
        if len(stack) == 0 and flag == 0:
            answer += 1
            
        s = s[1:] + s[0]
     
    return answer