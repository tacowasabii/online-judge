def solution(number, k):
    stack = []  # 숫자들을 저장할 스택
    for n in number:
        # 스택이 비어있지 않고, k가 0보다 크며, 스택의 마지막 숫자가 현재 숫자보다 작은 경우
        while stack and k > 0 and stack[-1] < n:
            stack.pop()  # 스택의 마지막 숫자를 제거
            k -= 1  # 제거할 숫자의 개수를 하나 줄임
        stack.append(n)  # 현재 숫자를 스택에 추가
    
    # k가 0보다 크다면(아직 제거할 숫자가 남아 있다면), 스택의 끝에서 k개의 숫자를 제거
    if k > 0:
        stack = stack[:-k]
    
    # 스택에 남아 있는 숫자들을 이어 붙여 문자열로 반환
    return ''.join(stack)
