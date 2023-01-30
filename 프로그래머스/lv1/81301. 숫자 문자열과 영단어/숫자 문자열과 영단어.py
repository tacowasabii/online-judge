def solution(s):
    answer = ''
    alp = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
           'eight': '8', 'nine': '9'}
    stack = []
    for i in s:
        if i.isalpha():
            stack.append(i)
            num = ''.join(stack)
            if num in alp:
                answer += alp[num]
                stack = []
        else:
            answer += i
    return int(answer)